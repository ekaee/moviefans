# Generated by Django 3.1.5 on 2021-08-05 14:16

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
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('slug', models.SlugField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(max_length=2000)),
                ('thumbnail', models.ImageField(blank=True, default='movie_icon.png', upload_to='movie_thumbnails/')),
                ('rating', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=2021)),
                ('slug', models.SlugField(unique=True)),
                ('views', models.IntegerField(default=0)),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=2000)),
                ('username', models.CharField(default='Unknown User', max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('upvote', models.IntegerField(default=0)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie')),
                ('user_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
