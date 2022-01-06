from django import forms
from django.contrib.auth.models import User
from .models import Business, NeighbourHood, Post, Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = ['name','location','admin','photo','description','health_toll','police_toll']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','email','description','neighbourhood','user']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','image','hood','user']
        


