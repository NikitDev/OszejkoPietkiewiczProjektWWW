from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission


@receiver(post_migrate)
def create_permission_groups(sender, **kwargs):
    if kwargs.get('app_config') and kwargs['app_config'].name == 'movieRentalApp':
        permissions = [
            'movieRentalApp.view_address',
            'movieRentalApp.change_address',
            'movieRentalApp.add_address',
            'movieRentalApp.delete_address',
            'movieRentalApp.view_category',
            'movieRentalApp.view_client',
            'movieRentalApp.change_client',
            'movieRentalApp.view_language',
            'movieRentalApp.view_movie',
            'movieRentalApp.view_moviedetails',
            'movieRentalApp.view_movierental',
        ]

        group, _ = Group.objects.get_or_create(name='Clients')

        for permission_code in permissions:
            app_label, codename = permission_code.split('.')
            permission = Permission.objects.get(content_type__app_label=app_label, codename=codename)
            group.permissions.add(permission)
