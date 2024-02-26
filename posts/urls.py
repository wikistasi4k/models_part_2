from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, AuthorListView, AuthorDetailView, AuthorCreateView

urlpatterns = [
    path('post-list/', PostListView.as_view(), name='post_list'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post-create/', PostCreateView.as_view(), name='post_create'),
    path('author-list/', AuthorListView.as_view(), name='author_list'),
    path('author-detail/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('author-create/', AuthorCreateView.as_view(), name='author_create'),
]
