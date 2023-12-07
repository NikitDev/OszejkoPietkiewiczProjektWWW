from django.contrib import admin
from .models import Client
from .models import Movie
from .models import MovieRental
from .models import MovieDetails
from .models import Language
from .models import Address
from .models import Category


admin.site.register(Client)
admin.site.register(Movie)
admin.site.register(MovieRental)
admin.site.register(MovieDetails)
admin.site.register(Language)
admin.site.register(Address)
admin.site.register(Category)
