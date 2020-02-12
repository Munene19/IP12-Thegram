from django.shortcuts import render, redirect
from .models import Profile
from .forms import *

def signup(request):
    context = {}
    return render(request, 'sign-up.html', context)

def index(request):
    context = {}
    return render(request, 'registration/login.html', context)

@login_required()
def edit_profile(request):
    if request.method == "POST"
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form. is valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success (request, "Profile updated!")
            return redirect ("edit_profile")
        else:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        context = {
            "user_form": user_form,
            "profile_form": profile_form
        }
        return render(request, "edit_profile.html", context)

@login_required()
def upload(request):
    if request.method == "POST"
    upload_form = upload_form(request.POST, request.FILES)
    if upload_form is_valid():
        upload_from.save()
        return redirect("")
    else:
        upload_form=uploadform()
    return render (request, "upload.html", {"upload_form":upload_form})