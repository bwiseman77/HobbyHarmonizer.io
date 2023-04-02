# Generated by Django 4.1.7 on 2023-04-02 06:37

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('HappyHobby', '0009_remove_profile_password_remove_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='picture',
        ),
        migrations.AddField(
            model_name='event',
            name='raised_money',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='event',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('a', 'cooking🍳'), ('b', 'fitness⚽️'), ('c', 'social🗣️'), ('d', 'nature🌳'), ('e', 'art🎨'), ('f', 'cultural🌈'), ('g', 'animals🐶'), ('h', 'ctive💃'), ('i', 'chill😌'), ('j', 'educational📚')], max_length=20, null=True),
        ),
    ]
