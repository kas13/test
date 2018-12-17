from django.shortcuts import redirect
from django import forms
from .models import Post, UserCreation, Subject

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = UserCreation
        fields = ('name', 'email', 'password',)


class SubjectCreationForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('name',)


# class SubjectCreationForm(forms.Form):
# 	subject = forms.CharField(max_length=20)