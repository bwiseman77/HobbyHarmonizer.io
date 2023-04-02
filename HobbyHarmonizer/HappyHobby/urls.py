from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

app_name = "HappyHobby"

urlpatterns = [
   path("login/", views.login_view, name="login"),
   path("signup/", views.signup, name='signup'),
   path("dashboard/", views.dashboard_view, name="dashboard"),
   path("picture/", views.CreatePostView.as_view(), name="add_picture"),
   path("logout/", views.logout_view, name="logout"),
   # path('login/', auth_views.LoginView.as_view(template_name='HobbyHarmonizer/login.html')),
]
