from django.contrib import admin

from .models import Profile,Event,Image
# Register your models here.

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Image)

