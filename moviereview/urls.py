from . import views
from .views import SearchResultsView, MovieDetailView
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('search/movie/<int:movie_id>/', MovieDetailView.as_view(), name='moviedetail')
]
