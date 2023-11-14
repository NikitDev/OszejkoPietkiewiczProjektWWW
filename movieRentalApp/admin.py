from django.contrib import admin
from .models import Client, Movie, MovieRental, MovieDetails, Language


admin.site.register(Client)
admin.site.register(Movie)
admin.site.register(MovieRental)
admin.site.register(MovieDetails)
admin.site.register(Language)
