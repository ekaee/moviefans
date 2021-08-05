from django.contrib import admin
from main.models import UserProfile, Movie, Genre, Comments

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)


class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre, GenreAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comments, CommentAdmin)
