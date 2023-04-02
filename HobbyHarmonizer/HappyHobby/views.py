from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from HappyHobby.forms import SignUpForm
from django.views.generic import CreateView, DetailView, ListView
from .models import Image, Event
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

class DashboardEventList(ListView):
    model = Event
    paginate_by = 20
    context_object_name = 'event_list'
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

    def get_queryset(self):
        if "R_filtertype" in self.request.session:
            filter_type = self.request.session["R_filtertype"];
        else:
            filter_type = ""

        if filter_type == "all":
            return posts.order_by('event_date')
        elif filter_type == "active":
            return posts.filter(post_status=True)
        elif filter_type == "inactive":
            return posts.filter(post_status=False)
        elif filter_type == "interested":
            return posts.exclude(post_interested_candidates=None)
        else:
            return posts.order_by('post_expiration')



def registeredEvents_view(request):
    return render(request, 'registeredEvents.html/')

def hostedEvents_view(request):
    return render(request, 'hostedEvents.html/')

def detailView_view(request):
    return render(request, 'detailView.html/')

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
            login(request, user)
            return redirect('/picture')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class CreateImageView(CreateView):  # new
    model = Image
    form_class = forms.ImageForm
    template_name = "picture.html"
    success_url = reverse_lazy("HappyHobby:dashboard")

    def form_valid(self, form):
        response = super(CreateImageView, self).form_valid(form)
        obj = form.save()
        self.request.user.profile.image = obj
        print(self.request.user)
        #self.request.user.profile.save()
        #self.request.user.save()
        obj.profile = self.request.user.profile
        obj.profile.save()
        obj.save()
        return response

class UserEventListView(LoginRequiredMixin, ListView):
    model = Event # query the post model to create the list of articles
    template_name = 'profile.html'
    context_object_name = 'events' # if I don't set context_object_name here, it will be object_list to iterate through the list of posts in the html page.
    ordering = ['-creation_date']

    # return the list of items for this view
    def get_queryset(self):
        # return Post.objects.filter(author = self.request.user, approved=True) 
        return Event.objects.filter(author = self.request.user.profile)

class CreateEventView(CreateView):
    model = Event
    form_class = forms.EventForm
    template_name = "create_event.html"
    success_url = reverse_lazy("HappyHobby:dashboard")

    def form_valid(self, form):
        response = super(CreateEventView, self).form_valid(form)
        obj = form.save(commit=False)
        obj.author=self.request.user.profile
        obj.save()
        return response


class EventDetailView(DetailView):
    model = Event
    form_class = forms.EventForm

class EventListView(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'dashboard.html'
    ordering = ['-creation_date']
    print('hi')

    def get_queryset(self):
        print('hi')
        return Event.objects.all()

