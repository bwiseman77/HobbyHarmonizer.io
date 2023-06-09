from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

app_name = "HappyHobby"

urlpatterns = [
   path("login/", views.login_view, name="login"),
   path("signup/", views.signup, name='signup'),

   path("dashboard/", views.EventListView.as_view(), name="dashboard"),
   path("picture/", views.CreateImageView.as_view(), name="add_picture"),
   path("createEvent/", views.CreateEventView.as_view(), name="create_event"),
   path('event/<int:pk>/', views.EventDetailView.as_view(), name="detailEvent"),
   path('donate/<int:pk>/', views.donate, name='donate'),

   path('filter', views.tag_filter, name="filter"),
   path("profile/", views.UserEventListView.as_view(), name="profile"),
   path("logout/", views.logout_view, name="logout"),
   path("registeredEvents/", views.EventListView_Registered.as_view(), name="registeredEvents"),
   path("hostedEvents/", views.EventListView_Hosted.as_view(), name="hostedEvents"),
]
