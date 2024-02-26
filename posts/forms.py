from django import forms
from .models import Post, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nick', 'email', 'bio']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
