from django import forms
from . models import Image,Profile,Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistration(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','likes','comments','user']
        
class ImageProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','image','date_posted']