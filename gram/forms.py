from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta
        model = User
        fieds = ["username", "email", "password1", "password2"]

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','likes','comments','user']
        
class ImageProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','image','timestamp']

class UserUpdateForm(Forms.ModelForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ["image"]
    
 class ProfileUpdateForm(Forms.ModelForm):
    class Meta: 
        model = Image
        fields = ["image"]

class UploadForm(forms.ModelForm)
    class Meta:
        model = Image
        fields = ["image","image_caption"]