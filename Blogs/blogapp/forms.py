# forms.py

from django import forms
from .models import Category, Post

class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description', 'url', 'image']

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'url', 'cat', 'image']

from django import forms
from .models import Category, Post

