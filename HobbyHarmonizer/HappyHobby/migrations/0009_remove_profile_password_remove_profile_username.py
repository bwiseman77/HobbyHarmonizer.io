# Generated by Django 4.1.7 on 2023-04-02 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HappyHobby', '0008_image_alter_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
