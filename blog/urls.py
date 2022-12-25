from django.urls import path
from . import views
from .views import (
    PostExploreView,
    PostListView,
    PostCreateView,
    PostDetailView,
    UserPostListView,
    PostUpdateView,
    PostDeleteView
)




urlpatterns = [
    path('explore/', PostExploreView.as_view(), name='explore'),
    path('home/', PostListView.as_view(), name='blog-home'),
    path('newpost/', PostCreateView.as_view(), name='post_form'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('user/<str:username>/', UserPostListView.as_view(), name='all_user_posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'), 
    ]

