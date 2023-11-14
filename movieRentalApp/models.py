from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Movie(models.Model):
    title = models.CharField(blank=False, null=False)
    description = models.CharField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    in_stock = models.IntegerField(default=0)


class MovieDetails(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, blank=False, null=False)
    rating = models.FloatField(default=0)
    production_year = models.IntegerField(blank=False, null=True)
    dubbing = models.ManyToManyField('Language', blank=True, related_name='moviedetails_dubbing')
    subtitles = models.ManyToManyField('Language', blank=True, related_name='moviedetails_subtitles')
    pegi = models.IntegerField(default=18)
    movie_length = models.IntegerField()
    languages = models.ManyToManyField('Language', blank=False, related_name='moviedetails_languages')


class Language(models.Model):
    language = models.CharField(blank=False, null=False)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True, null=True)


class MovieRental(models.Model):
    class StatusChoices(models.TextChoices):
        RENTED = 'REN', 'RENTED'
        RETURNED = 'RET', 'RETURNED'

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    status = models.CharField(choices=StatusChoices.choices, default=StatusChoices.RENTED)
    date_start = models.DateField(default=timezone.now)
    date_end = models.DateField(blank=True, null=True)
    days_rented = models.IntegerField(default=1)
