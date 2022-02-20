"""League app."""

# Django
from django.apps import AppConfig


class LeagueAppConfig(AppConfig):
    """League app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = 'volleyball.league'
    verbose_name = 'Leagues'

    '''
    def ready(self):
        """Load signals."""
        import volleyball.league.signals  # noqa
        super().ready()
    '''