from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from main.models import Movie, UserProfile
from django.contrib.auth.forms import UserCreationForm

# user auth form
class UserForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("picture",)

# add_movie html poge
class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = (
            "name",
            "genre_id",
            "description",
            "thumbnail",
            "year",
        )
        exclude = (
            "slug",
            "rating",
            "views",
        )
