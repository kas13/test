from django.shortcuts import redirect
from django import forms

from .models import Post, UserCreation

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = UserCreation
        fields = ('name', 'email', 'password',)

