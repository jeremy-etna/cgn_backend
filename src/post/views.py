from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)

from post.forms import PostForm
from post.models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "feed.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["role"] = self.request.user.role
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("feed")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["role"] = self.request.user.role
        return context


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "posts_owner.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["role"] = self.request.user.role
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post_create.html"
    fields = ["title", "content", "tags", "image", "video_url", "social_link"]

    def get_success_url(self):
        return reverse_lazy("posts-owner")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["role"] = self.request.user.role
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('posts-owner')
