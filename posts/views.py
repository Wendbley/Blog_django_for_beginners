from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    
class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = "post_detail.html"
