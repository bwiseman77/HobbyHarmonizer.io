from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):

    name = forms.CharField(max_length=30, required=True)
    bio = forms.CharField(max_length=300, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'bio',)

        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title", "image"]

class EventForm(forms.ModelForm):

    event_date = forms.DateTimeField(help_text='format: yyyy-mm-dd')
    class Meta:
        model = Event
        fields = ["event_title","event_date", "location", "description", "tags","charity",]
