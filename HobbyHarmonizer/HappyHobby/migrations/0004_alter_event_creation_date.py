# Generated by Django 4.1 on 2023-04-01 02:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HappyHobby', '0003_alter_event_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
