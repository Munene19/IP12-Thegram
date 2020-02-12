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
    profile_form = 