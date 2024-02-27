# accounts/views.py
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from . import models
from .forms import SignupForm
from .models import Profile



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user=form.cleaned_data.get('Username')
            # password=form.cleaned_data.get('Password')
            login(request, user)
            return redirect('\products')  # Redirect to your desired page after successful signup
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})




def profile(request):
    profile = get_object_or_404(Profile)
    return render(request, 'profile.html', {'profile': profile})