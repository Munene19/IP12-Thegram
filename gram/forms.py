from django import forms
from . models import *

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
    