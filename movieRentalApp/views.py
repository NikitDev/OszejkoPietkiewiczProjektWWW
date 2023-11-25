from django.http import Http404
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Movie
from .models import Language
from .models import MovieDetails
from .models import MovieRental
from .models import Address
from .models import Client
from .models import Category

from .serializers import MovieSerializer
from .serializers import MovieRentalSerializer
from .serializers import MovieDetailsSerializer
from .serializers import LanguageSerializer
from .serializers import ClientSerializer
from .serializers import AddressSerializer
from .serializers import CategorySerializer


class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


class MovieListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return Movie.objects.all()

    def get(self, request):
        movies = self.get_queryset().order_by('id')
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return MovieDetails.objects.all()

    def get_object(self, pk):
        try:
            return self.get_queryset().get(pk=pk)
        except MovieDetails.DoesNotExist:
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
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return MovieRental.objects.all()
        return MovieRental.objects.filter(client=self.request.user.client)

    def get(self, request):
        movie_rentals = self.get_queryset().order_by('id')
        serializer = MovieRentalSerializer(movie_rentals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieRentalSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieRentalDetailsView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return MovieRental.objects.all()
        return MovieRental.objects.filter(client=self.request.user.client)

    def get_object(self, pk):
        try:
            return self.get_queryset().get(pk=pk)
        except MovieRental.DoesNotExist:
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
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return MovieDetails.objects.all()

    def get(self, request):
        movie_details = self.get_queryset().order_by('id')
        serializer = MovieDetailsSerializer(movie_details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieDetailsSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsDetailsView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return MovieDetails.objects.all()

    def get_object(self, pk):
        try:
            return self.get_queryset().get(pk=pk)
        except MovieDetails.DoesNotExist:
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
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return Language.objects.all()

    def get(self, request):
        languages = self.get_queryset().order_by('id')
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LanguageSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LanguageDetailsView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return Language.objects.all()

    def get_object(self, pk):
        try:
            return self.get_queryset().get(pk=pk)
        except Language.DoesNotExist:
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


class ClientListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Client.objects.all()
        return Client.objects.filter(user=self.request.user)

    def get(self, request):
        clients = self.get_queryset().order_by('id')
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailsView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Client.objects.all()
        return Client.objects.filter(user=self.request.user)

    def get_object(self, pk):
        try:
            return self.get_queryset().get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return Category.objects.all()

    def get(self, request):
        categories = self.get_queryset().order_by('id')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailsView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return Category.objects.all()

    def get_object(self, pk):
        try:
            return self.get_queryset().get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddressListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Address.objects.all()
        return Address.objects.filter(client=self.request.user.client)

    def get(self, request):
        address = self.get_queryset().order_by('id')
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddressSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressDetailsView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Address.objects.all()
        return Address.objects.filter(client=self.request.user.client)

    def get_object(self, pk):
        try:
            return self.get_queryset().get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        address = self.get_object(pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, pk):
        address = self.get_object(pk)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)