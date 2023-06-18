from . import views
from .views import SearchResultsView, MovieDetailView, HomeView, AddReviewView, EditReviewView
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('search/movie/<int:movie_id>/', MovieDetailView.as_view(), name='moviedetail'),
    path('search/movie/<int:movie_id>/movie/addreview/', AddReviewView.as_view(), name='addreview'),
    path('edit/<review_id>', EditReviewView.as_view(), name='edit'),
]
