from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    paginate_by = 1
    context_object_name = 'post'
    queryset = Post.objects.filter(publick=True)
    template_name = 'posts/post_list.html'


class PostDetail(DetailView):
    model = Post
    context_object_name = 'content'
    slug_field = 'slug'
    template_name = 'posts/post_detail.html'





