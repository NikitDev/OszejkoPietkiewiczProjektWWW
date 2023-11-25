from rest_framework.serializers import ModelSerializer

from .models import Movie
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

