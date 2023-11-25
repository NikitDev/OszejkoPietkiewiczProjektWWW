from rest_framework.serializers import ModelSerializer

from .models import Movie, Address, Category, Client
from .models import Language
from .models import MovieDetails
from .models import MovieRental


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = [
            'id',
        ]


class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
        read_only_fields = [
            'id',
        ]


class MovieDetailsSerializer(ModelSerializer):
    class Meta:
        model = MovieDetails
        fields = '__all__'
        read_only_fields = [
            'id',
        ]


class MovieRentalSerializer(ModelSerializer):
    class Meta:
        model = MovieRental
        fields = '__all__'
        read_only_fields = [
            'id',
        ]


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = [
            'id',
        ]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = [
            'id',
        ]


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = [
            'id',
        ]
