from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

app_name = "HappyHarmonizer"

urlpatterns = [
   path("login/", views.login_view, name="login"),
   # path('login/', auth_views.LoginView.as_view(template_name='HobbyHarmonizer/login.html')),
]
