from django.db import models
from django.template.defaultfilters import default, slugify
from django.contrib.auth.models import User
from django.urls.base import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

# Global Variables
NAME_MAX_LENGTH = 128
CONTENT_MAX_LENGTH = 2000

# Django - user model modification
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile_images", blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.user.username


# movie categories model
class Genre(models.Model):

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("main:genre", args=[str(self.slug)])

    def __str__(self):
        return self.name

# movie model / connected to genre model
class Movie(models.Model):
    DESCRIPTION_MAX_LENGTH = 200

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.CharField(max_length=CONTENT_MAX_LENGTH)
    thumbnail = models.ImageField(
        upload_to="thumbnail_upload/",
        blank=True,
        default="movie_icon.png",
    )
    rating = models.IntegerField(default=0)  # likes
    year = models.IntegerField(default=2021)
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("main:movie", args=[str(self.slug)])

    def __str__(self):
        return self.name


# comment model associated with movie and user models
class Comments(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=CONTENT_MAX_LENGTH, default="")  # comment
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    username = models.CharField(default="Unknown User", max_length=20)
    time = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(default=0)
