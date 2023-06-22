from . import views
from .views import SearchResultsView, MovieDetailView, HomeView, AddReviewView, EditReviewView, DeleteReviewView, ReviewLike
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('search/movie/<int:movie_id>/', MovieDetailView.as_view(), name='moviedetail'),
    path('search/movie/<int:movie_id>/addreview/', AddReviewView.as_view(), name='addreview'),
    path('search/movie/<int:movie_id>/edit/<review_id>', EditReviewView.as_view(), name='edit'),
    path('search/movie/<int:movie_id>/delete/<review_id>', DeleteReviewView.as_view(), name='delete'),
    path('like/<review_id>', ReviewLike.as_view(), name='review_like')
]
