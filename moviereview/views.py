import requests
import os
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Review, ReviewLikes
from .forms import ReviewForm
from django.contrib import messages
from django.db.models import Avg, Count

import pandas as pd


api_key = os.environ.get('MY_API_KEY')

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}


class HomeView(TemplateView):
    """ View to render the homepage """
    template_name = 'index.html'


class SearchResultsView(View):
    """ View to render movie search results """
    template_name = 'search_results.html'
    paginate_by = 9

    def get(self, request, *args, **kwargs):
        """
        Gets the users search query and
        returns a list of movies from the TMDB API
        """
        data = None
        query = request.GET.get('q')
        page = request.GET.get('p')
        url = f"https://api.themoviedb.org/3/search/movie?query={query}&api_key={api_key}&include_adult=false&language=en-US&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json

        return render(request, 'search_results.html', {
            "data": data,
        })


class MovieDetailView(View):
    """ View to render movie data and review data """
    template_name = 'movie_detail.html'

    def get(self, request, movie_id, *args, **kwargs):
        """
        Gets movie detail data from the TMDB API
        and movie reviews from the database
        """
        # API request for movie data
        data = None
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?&api_key={api_key}&language=en-US&page=1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json

        # Get movie reviews from the database
        movie_id = movie_id
        reviews = Review.objects.filter(movie_id=f'{movie_id}')

        # Calculate the average movie rating
        rating = Review.objects.filter(
            movie_id=f'{movie_id}').aggregate(Avg("rating"))
        rating = str(rating['rating__avg'])[0:3]

        # Calculate total review likes
        total_likes = ReviewLikes.objects.all().values('review').annotate(
            total=Count('id')
        )
        dict_review_id_to_total_likes = {}
        for t in total_likes:
            dict_review_id_to_total_likes[t['review']] = t['total']

        # Parse data models to pandas df
        df_likes = pd.DataFrame(list(ReviewLikes.objects.all().values()))
        df_reviews = pd.DataFrame(list(Review.objects.all().values()))

        # Map reviews to likes
        df_reviews_and_likes = pd.merge(
            df_reviews[['id']],
            df_likes[['review_id', 'voter_id']],
            left_on=['id'],
            right_on=['review_id'],
            how='left'
        )

        map_review_id_to_voter_id = {}
        for review_id_iterator in df_reviews_and_likes['id'].unique():
            # Filter rows in ReviewLikes for a given review
            df_likes_review_id = \
                df_reviews_and_likes[
                    df_reviews_and_likes['review_id'] == review_id_iterator
                ]

            # Get list of voters that liked that review
            voters_for_review_id = \
                list(df_likes_review_id['voter_id'].unique())

            # Update map with review_id (key) and list of voters (value)
            map_review_id_to_voter_id[review_id_iterator] = \
                voters_for_review_id

        return render(request, 'movie_detail.html', {
            "data": data,
            "reviews": reviews,
            "rating": rating,
            "total_likes": dict_review_id_to_total_likes,
            "map_review_id_to_voter_id": map_review_id_to_voter_id
        })


class AddReviewView(View):
    """ View to add a new movie review """

    def get(self, request, movie_id, *args, **kwargs):
        """ Get the review form and render add_review page """

        reviewform = ReviewForm()

        return render(request, 'add_review.html', {
            "review_form": ReviewForm()
            })

    def post(self, request, movie_id, *args, **kwargs):
        """
        Create a new review for the movie, store it
        in the database and redirect the user back to
        the relevant movie detail page
        """

        reviewform = ReviewForm(data=request.POST)

        if reviewform.is_valid():
            reviewform.instance.author = request.user
            review = reviewform.save(commit=False)
            review.movie_id = movie_id
            review.save()
            messages.success(
                request, "Your review has been sucessfully added."
            )
        else:
            reviewform = ReviewForm()

        return HttpResponseRedirect(reverse("moviedetail", args=[movie_id]))


class EditReviewView(View):
    """
    View to edit reviews
    """
    def get(self, request, review_id, *args, **kwargs):
        """
        Render edit_review page and get review form
        populated with the data from the initial review
        """
        review = get_object_or_404(Review, id=review_id)
        reviewform = ReviewForm(instance=review)

        return render(request, 'edit_review.html', {
            "review_form": reviewform,
            "review": review
            })

    def post(self, request, review_id, movie_id, *args, **kwargs):
        """
        Update the review in the database and redirect user
        back to the movie detail page
        """
        review = get_object_or_404(Review, id=review_id)
        reviewform = ReviewForm(instance=review, data=request.POST)

        if reviewform.is_valid():
            reviewform.instance.author = request.user
            review = reviewform.save(commit=False)
            review.movie_id = movie_id
            review.save()
            messages.success(
                request, "Your review has been sucessfully updated."
            )
        else:
            reviewform = ReviewForm()

        return HttpResponseRedirect(reverse("moviedetail", args=[movie_id]))


class DeleteReviewView(View):
    """
    View to delete a review from the database
    """

    def get(self, request, review_id, *args, **kwargs):
        """ render delete_review.html """
        queryset = Review.objects.all()
        review = get_object_or_404(queryset, id=review_id)

        return render(request, 'delete_review.html', {
            "review": review,
            })

    def post(self, request, review_id, movie_id, *args, **kwargs):
        """
        delete the review and redirec the user back to the movie detail page
        """
        queryset = Review.objects.all()
        review = get_object_or_404(queryset, id=review_id)
        movie_id = review.movie_id
        review.delete()
        messages.success(request, "Your review has been deleted.")

        return HttpResponseRedirect(reverse("moviedetail", args=[movie_id]))


class ReviewLike(View):
    """
    View to add and remove review likes from the database
    """

    def post(self, request, review_id):
        """
        Add and delete review likes to/from the database
        """
        review = get_object_or_404(Review, id=review_id)
        movie_id = review.movie_id
        voter = request.user

        # check if the user has already liked the review
        # if they have, delete the review like object from the database
        try:
            liked_review = ReviewLikes.objects.get(voter=voter, review=review)
            liked_review.delete()

        # if the user has not liked the review,
        # add a new review like object to the database
        except ReviewLikes.DoesNotExist:
            ReviewLikes.objects.create(voter=voter, review=review, likes=1)

        return HttpResponseRedirect(reverse("moviedetail", args=[movie_id]))
