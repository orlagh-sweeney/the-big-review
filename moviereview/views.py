import requests
import os
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Review, ReviewLikes


api_key = os.environ.get('MY_API_KEY')

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}


class HomeView(TemplateView):
    template_name = 'index.html'


class SearchResultsView(View):
    template_name = 'search_results.html'
    paginate_by = 6
    print('test 1')

    def get(self, request, *args, **kwargs):
        data = None
        query = request.GET.get('q')
        url = f"https://api.themoviedb.org/3/search/movie?query={query}&api_key={api_key}&include_adult=false&language=en-US&page=1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json
            print(response.text)

        return render(request, 'search_results.html', {
            "data": data,
        })
