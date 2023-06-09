# Generated by Django 4.1.7 on 2023-04-02 06:46

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('HappyHobby', '0010_remove_event_picture_event_raised_money_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('a', 'cooking🍳'), ('b', 'fitness⚽️'), ('c', 'social🗣️'), ('d', 'nature🌳'), ('e', 'art🎨'), ('f', 'cultural🌈'), ('g', 'animals🐶'), ('h', 'ctive💃'), ('i', 'chill😌'), ('j', 'educational📚')], max_length=20, null=True),
        ),
    ]
