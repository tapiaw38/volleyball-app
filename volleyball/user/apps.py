"""Users app."""

# Django
from django.apps import AppConfig


class UserAppConfig(AppConfig):
    """Users app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = 'volleyball.user'
    verbose_name = 'Users'
