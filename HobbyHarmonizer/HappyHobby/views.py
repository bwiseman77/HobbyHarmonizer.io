from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from HappyHobby.forms import SignUpForm

def login_view(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate (
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is None:
                message = "Login Failed"
                print("login failed :-(")
            else:
                login(request, user)
                message = f"Hello {user.username}!"
                print("login success :-)")
                return redirect("/dashboard")
            
    return render(request, 'login.html/', context={'form': form, 'message' : message})

def dashboard_view(request):
    return render(request, 'dashboard.html/')

def registeredEvents_view(request):
    return render(request, 'registeredEvents.html/')

def hostedEvents_view(request):
    return render(request, 'hostedEvents.html/')

def logout_view(request):
    print("logging out")
    logout(request)
    return redirect("/login")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() # load profile
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.email = form.cleaned_data.get('email')
            #user.profile.picture = form.cleaned_data.get('picture')
            user.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
