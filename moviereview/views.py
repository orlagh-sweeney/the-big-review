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
from django.db.models import Avg
from django.db.models.functions import Round


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
    print('test 1')

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
            print(response.text)

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
        data = None
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?&api_key={api_key}&language=en-US&page=1"
        response = requests.get(url)
        print(response)

        if response.status_code == 200:
            data = response.json
            print(response.text)

        movie_id = movie_id
        reviews = Review.objects.filter(movie_id=f'{movie_id}')
        rating = Review.objects.filter(movie_id=f'{movie_id}').aggregate(Avg("rating"))
        rating = str(rating['rating__avg'])[0:3]

        return render(request, 'movie_detail.html', {
            "data": data,
            "reviews": reviews,
            "rating": rating,
        })


class AddReviewView(View):
    """ View to add a review to a movie """

    def get(self, request, movie_id, *args, **kwargs):
        """ Get review form and render add_review page """

        reviewform = ReviewForm()

        return render(request, 'add_review.html', {
            "review_form": ReviewForm()
            })

    def post(self, request, movie_id, *args, **kwargs):
        """
        Creates a new review for the movie, stores it
        in the database and redirects the user back to
        the relevant movie detail page
        """

        reviewform = ReviewForm(data=request.POST)  

        if reviewform.is_valid():
            reviewform.instance.author = request.user
            review = reviewform.save(commit=False)
            review.movie_id = movie_id
            review.save()
            messages.success(request, "Your review has been sucessfully added.")
        else:
            reviewform = ReviewForm()

        return HttpResponseRedirect(reverse("moviedetail", args=[movie_id]))


class EditReviewView(View):

    def get(self, request, review_id, *args, **kwargs):
        review = get_object_or_404(Review, id=review_id)
        reviewform = ReviewForm(instance=review)

        return render(request, 'edit_review.html', {
            "review_form": reviewform,
            "review": review
            })

    def post(self, request, review_id, movie_id, *args, **kwargs):
        review = get_object_or_404(Review, id=review_id)
        reviewform = ReviewForm(instance=review, data=request.POST)

        if reviewform.is_valid():
            reviewform.instance.author = request.user
            review = reviewform.save(commit=False)
            review.movie_id = movie_id
            review.save()
            messages.success(request, "Your review has been sucessfully updated.")
        else:
            reviewform = ReviewForm()

        return HttpResponseRedirect(reverse("moviedetail", args=[movie_id]))


class DeleteReviewView(View):

    def get(self, request, review_id, *args, **kwargs):
        queryset = Review.objects.all()
        review = get_object_or_404(queryset, id=review_id)

        return render(request, 'delete_review.html', {
            "review": review,
            })

    def post(self, request, review_id, movie_id, *args, **kwargs):
        queryset = Review.objects.all()
        review = get_object_or_404(queryset, id=review_id)
        movie_id = review.movie_id
        review.delete()
        messages.success(request, "Your review has been deleted.")

        return HttpResponseRedirect(reverse("moviedetail", args=[movie_id]))


class ReviewLike(View):

    def post(self, request, review_id):

        review = get_object_or_404(Review, id=review_id)
        movie_id = review.movie_id
        voter = request.user

        total_likes = ReviewLikes.objects.filter(review=review).count()
        print(total_likes)

        try:
            liked_review = ReviewLikes.objects.get(voter=voter, review=review)
            liked_review.delete()
            total_likes = total_likes - 1
        except ReviewLikes.DoesNotExist:
            ReviewLikes.objects.create(voter=voter, review=review, likes=1)
            total_likes = total_likes + 1

        return HttpResponseRedirect(reverse("moviedetail", args=[movie_id]))
