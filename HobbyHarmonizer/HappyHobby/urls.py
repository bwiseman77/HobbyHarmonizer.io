from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from django.conf.urls.static import static

app_name = "HappyHarmonizer"

urlpatterns = [
   path("login/", views.login_view, name="login"),
   path("register/", views.register, name='register'),
   path("dashboard/", views.dashboard_view, name="dashboard"),
   path("logout/", views.logout_view, name="logout"),
   # path('login/', auth_views.LoginView.as_view(template_name='HobbyHarmonizer/login.html')),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)

# Only add this when we are in debug mode.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
