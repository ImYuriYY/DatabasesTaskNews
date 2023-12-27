from django import forms
from .models import *


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'add-post-title',
                'placeholder': 'Title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'add-post-content',
                'placeholder': 'Content'
            }),
            'author': forms.Select(attrs={
                'class': 'add-post-author',
            }),
        }