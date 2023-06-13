from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        exclude = [
            'author',
            'created_at',
            'updated_at',
            'likes'
        ]