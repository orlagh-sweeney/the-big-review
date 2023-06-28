from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'search/',
        views.SearchResultsView.as_view(),
        name='search'
    ),
    path(
        'search/movie/<int:movie_id>/',
        views.MovieDetailView.as_view(),
        name='moviedetail'
    ),
    path(
        'search/movie/<int:movie_id>/addreview/',
        views.AddReviewView.as_view(),
        name='addreview'
    ),
    path(
        'search/movie/<int:movie_id>/edit/<review_id>',
        views.EditReviewView.as_view(),
        name='edit'
    ),
    path(
        'search/movie/<int:movie_id>/delete/<review_id>',
        views.DeleteReviewView.as_view(),
        name='delete'
    ),
    path(
        'like/<review_id>',
        views.ReviewLike.as_view(),
        name='review_like'
    )
]
