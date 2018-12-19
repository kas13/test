from django.shortcuts import redirect
from django import forms
from .models import Post, UserCreation, SubjectList

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
        model = SubjectList
        fields = ('name',)

class CreateQuestionForm(forms.Form):
	question = forms.CharField(widget=forms.Textarea)
	variants = forms.CharField(widget=forms.Textarea)
	answer   = forms.CharField(max_length=200)

# class SubjectCreationForm(forms.Form):
# 	subject = forms.CharField(max_length=20)