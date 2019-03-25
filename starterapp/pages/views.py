from django.shortcuts import render
from .models import Pages
from django.views.generic import ListView, DetailView

# Create your views here.

class Page_Detail(DetailView):
    model = Pages
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    context_object_name = 'page'
     # if pagination is desired


