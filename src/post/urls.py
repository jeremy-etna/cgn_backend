from django.urls import path
from post.views import (
    PostListView,
    PostCreateView,
    UserPostListView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='feed'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('owner/', UserPostListView.as_view(), name='posts-owner'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
