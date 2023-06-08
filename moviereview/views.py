from django.shortcuts import render
import requests
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Review, ReviewLikes


class HomeView(TemplateView):
    template_name = 'index.html'
