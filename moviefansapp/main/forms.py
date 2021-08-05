from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from main.models import Movie, UserProfile
from django.contrib.auth.forms import UserCreationForm


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


class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = (
            "slug",
            "rating",
            "views",
        )

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     url = cleaned_data.get("url")

    #     if url and not url.startswith("http://"):
    #         url = f"http://{url}"
    #         cleaned_data["url"] = url

    #     return cleaned_data
