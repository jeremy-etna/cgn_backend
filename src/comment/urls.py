from django.urls import path
from comment.views import (
    add_comment_to_post,
    get_comments,
)

urlpatterns = [
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/comment/<int:parent_comment_id>/', add_comment_to_post, name='add_reply_to_post_comment'),
    path('ajax/comments/<int:post_id>/', get_comments, name='get-comments'),
]
