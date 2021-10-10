from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [

    path('index/', views.index, name='blog-index'),
    path('index/diet.html', views.diet, name='blog-diet'),
]
