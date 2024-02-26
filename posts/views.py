from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Post, Author
from .forms import PostForm, AuthorForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

class AuthorListView(ListView):
    model = Author
    template_name = 'posts/author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'posts/author_detail.html'
    context_object_name = 'author'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'posts/author_create.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')
