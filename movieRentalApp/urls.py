from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import LanguageListView
from .views import LanguageDetailsView
from .views import MovieListView
from .views import MovieDetailsView
from .views import MovieRentalListView
from .views import MovieRentalDetailsView
from .views import MovieDetailsListView
from .views import MovieDetailsDetailsView
from .views import ClientListView
from .views import ClientDetailsView
from .views import AddressListView
from .views import AddressDetailsView
from .views import CategoryListView
from .views import CategoryDetailsView


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
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailsView.as_view(), name='client_details'),
    path('address/', AddressListView.as_view(), name='address_list'),
    path('address/<int:pk>/', AddressDetailsView.as_view(), name='address_details'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailsView.as_view(), name='category_details'),
    path('api-token-auth/', obtain_auth_token),
]
