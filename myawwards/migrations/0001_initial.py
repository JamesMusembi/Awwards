# Generated by Django 3.2.13 on 2022-06-11 19:37

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('Bio', models.CharField(max_length=30)),
                ('datecreated', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('projectscreenshot', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('projecturl', models.URLField()),
                ('datecreated', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='myawwards.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Revieww',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=3000)),
                ('design', models.PositiveSmallIntegerField(choices=[(1, '1- Trash'), (2, '2- Horrible'), (3, '3- Terrible'), (4, '4- Bad'), (5, '5- Ok'), (6, '6- Watchable'), (7, '7- Good'), (8, '8- Very Good'), (9, '9- perfect'), (10, '10- Master Piece')], default=0)),
                ('usability', models.PositiveSmallIntegerField(choices=[(1, '1- Trash'), (2, '2- Horrible'), (3, '3- Terrible'), (4, '4- Bad'), (5, '5- Ok'), (6, '6- Watchable'), (7, '7- Good'), (8, '8- Very Good'), (9, '9- perfect'), (10, '10- Master Piece')], default=0)),
                ('content', models.PositiveSmallIntegerField(choices=[(1, '1- Trash'), (2, '2- Horrible'), (3, '3- Terrible'), (4, '4- Bad'), (5, '5- Ok'), (6, '6- Watchable'), (7, '7- Good'), (8, '8- Very Good'), (9, '9- perfect'), (10, '10- Master Piece')], default=0)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myawwards.projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
