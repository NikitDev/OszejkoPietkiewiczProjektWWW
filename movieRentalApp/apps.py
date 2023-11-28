from django.apps import AppConfig


class MovierentalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movieRentalApp'

    def ready(self):
        import movieRentalApp.signals
