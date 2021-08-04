from django.db import models
from django.template.defaultfilters import default, slugify
from django.contrib.auth.models import User

NAME_MAX_LENGTH = 128
CONTENT_MAX_LENGTH = 2000


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile_images", blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.user.username


class Genre(models.Model):

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Movie(models.Model):
    DESCRIPTION_MAX_LENGTH = 200

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.CharField(max_length=CONTENT_MAX_LENGTH)
    thumbnail = models.ImageField(
        upload_to="movie_thumbnails/", blank=True, default="static/movie_icon.png"
    )
    rating = models.IntegerField(default=0)  # likes
    year = models.IntegerField(default=2021)
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comments(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=CONTENT_MAX_LENGTH, default="")  # comment
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(default=0)
