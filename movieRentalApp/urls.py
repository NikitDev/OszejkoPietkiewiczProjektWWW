from django.contrib import admin
from django.urls import path

from .views import LanguageListView
from .views import LanguageDetailsView
from .views import MovieListView
from .views import MovieDetailsView
from .views import MovieRentalListView
from .views import MovieRentalDetailsView
from .views import MovieDetailsListView
from .views import MovieDetailsDetailsView


app_mame = 'movieRentalApp'

urlpatterns = [
    path('language/', LanguageListView.as_view(), name='language_list'),
    path('language/<int:pk>/', LanguageDetailsView.as_view(), name='language_details'),
    path('movie/', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailsView.as_view(), name='movie_details'),
    path('movie-rental/', MovieRentalListView.as_view(), name='movie_rental_list'),
    path('movie-rental/<int:pk>/', MovieRentalDetailsView.as_view(), name='movie_rental_details'),
    path('movie-details/', MovieDetailsListView.as_view(), name='movie_details_list'),
    path('movie-details/<int:pk>/', MovieDetailsDetailsView.as_view(), name='movie_details_details'),
]
