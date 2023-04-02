from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from HappyHobby.forms import SignUpForm
from django.views.generic import CreateView
from .models import Image
from django.urls import reverse_lazy

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

def logout_view(request):
    print("logging out")
    logout(request)
    return redirect("/login")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.email = form.cleaned_data.get('email')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.name = form.cleaned_data.get('name')
            user.profile.save()
            user.save()
            #user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/picture')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class CreatePostView(CreateView):  # new
    model = Image
    form_class = forms.PostForm
    template_name = "picture.html"
    success_url = reverse_lazy("HappyHobby:dashboard")

    def form_valid(self, form):
        response = super(CreatePostView, self).form_valid(form)
        obj = form.save()
        self.request.user.profile.image = obj
        self.request.user.save()
        print(self.request)
        print(self.request.user)
        print("hello")
        self.request.user.profile.save()
        return response

        
