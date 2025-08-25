from django.urls import path
from .views import HomePageView
from .views import PostDetailView

urlpatterns = [
    
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", HomePageView.as_view(), name="home"),
]
