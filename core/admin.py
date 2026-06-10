from django.contrib import admin

from .models import Movie, MoviePerson, Person, Studio

# Register your models here.

admin.site.register(Studio)
admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(MoviePerson)
