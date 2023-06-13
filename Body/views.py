from django.shortcuts import render
from django.views.generic import ListView, DetailView

from Body.models import Post


# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-updated_at'

class PostDetail(DetailView):
    model = Post