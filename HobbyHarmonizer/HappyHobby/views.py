from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . import forms

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
            
    return render(request, 'login.html/', context={'form': form, 'message' : message})

def logout_view(request):
    logout(request)
