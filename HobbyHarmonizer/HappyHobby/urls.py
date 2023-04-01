from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

app_name = "HappyHarmonizer"

urlpatterns = [
   path("login/", views.login_view, name="login"),
   path("signup/", views.signup, name='signup'),
   path("dashboard/", views.dashboard_view, name="dashboard"),
   path("logout/", views.logout_view, name="logout"),
   path("registeredEvents/", views.registeredEvents_view, name="registeredEvents"),
   path("hostedEvents/", views.hostedEvents_view, name="hostedEvents"),
   # path('login/', auth_views.LoginView.as_view(template_name='HobbyHarmonizer/login.html')),
]
