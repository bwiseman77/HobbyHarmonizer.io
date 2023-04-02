from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Image(models.Model):
    title = models.TextField()
    image = models.ImageField(default='image.jpg', upload_to='images/')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.CharField(max_length=300)
    picture = models.OneToOneField(Image, on_delete=models.CASCADE, null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()       


class Tags(models.Model):
    name = models.CharField(max_length=20)


class Event(models.Model):
    event_date = models.DateTimeField(blank=False, null=False)
    creation_date = models.DateTimeField(default=now)
    author = models.ForeignKey(Profile, related_name='author', on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tags)
    '''
            max_length=30,
            choices=[
                "cooking",
                "fitness",
                "social",
                "nature",
                "art",
                "cultural",
                "animals",
                "active",
                "chill",
                "educational"
                ]
            )
    '''
    active = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='uploads/')
    charity = models.CharField(
            max_length=50,
            choices=[
                (1,"Boys & Girls Club of SB"),
                (2,"SB Center for the Homeless"),
                (3,"American Red Cross"),
                (4,"Salvation Army"),
                (5,"Native American Rights Fund"),
                (6,"St. Jude Children's Research Hospital"),
                (7,"Habitat for Humanity"),
                (8,"Wounded Warrior Project"),
                (9,"Humane Society"),
                (10,"Special Olympics")
                ]
            )

    registered_users = models.ManyToManyField(Profile, related_name='registered_users')

