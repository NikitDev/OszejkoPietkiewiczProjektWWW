from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Movie
from .models import Language
from .models import MovieDetails
from .models import MovieRental

from .serializers import MovieSerializer
from .serializers import MovieRentalSerializer
from .serializers import MovieDetailsSerializer
from .serializers import LanguageSerializer


class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all().order_by('id')
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsView(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieRentalListView(APIView):
    def get(self, request):
        movie_rentals = MovieRental.objects.all().order_by('id')
        serializer = MovieRentalSerializer(movie_rentals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieRentalSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieRentalDetailsView(APIView):
    def get_object(self, pk):
        try:
            return MovieRental.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie_rental = self.get_object(pk)
        serializer = MovieRentalSerializer(movie_rental)
        return Response(serializer.data)

    def put(self, request, pk):
        movie_rental = self.get_object(pk)
        serializer = MovieRentalSerializer(movie_rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie_rental = self.get_object(pk)
        movie_rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieDetailsListView(APIView):
    def get(self, request):
        movie_details = MovieDetails.objects.all().order_by('id')
        serializer = MovieDetailsSerializer(movie_details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieDetailsSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsDetailsView(APIView):
    def get_object(self, pk):
        try:
            return MovieDetails.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie_details = self.get_object(pk)
        serializer = MovieDetailsSerializer(movie_details)
        return Response(serializer.data)

    def put(self, request, pk):
        movie_details = self.get_object(pk)
        serializer = MovieDetailsSerializer(movie_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie_details = self.get_object(pk)
        movie_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LanguageListView(APIView):
    def get(self, request):
        languages = Language.objects.all().order_by('id')
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LanguageSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LanguageDetailsView(APIView):
    def get_object(self, pk):
        try:
            return Language.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    def put(self, request, pk):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        language = self.get_object(pk)
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# TODO: Client serializer and apiview, update models and add category model
