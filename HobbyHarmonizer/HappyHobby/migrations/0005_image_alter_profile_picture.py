# Generated by Django 4.1.7 on 2023-04-01 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HappyHobby', '0004_alter_event_creation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='uploads')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HappyHobby.image'),
        ),
    ]
