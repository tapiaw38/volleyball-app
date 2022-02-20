""" Match Model """

# Django.
from django.db import models

# Utilities
from volleyball.utils.models import BaseModel

# Create your models here.


class Match(BaseModel):
    """
    Match Model.
    """

    league = models.ForeignKey(
        'league.League',
        related_name='league',
        on_delete=models.CASCADE
    )

    home_team = models.ForeignKey(
        'league.Team',
        related_name='home_team',
        on_delete=models.CASCADE
    )

    away_team = models.ForeignKey(
        'league.Team',
        related_name='away_team',
        on_delete=models.CASCADE
    )

    date = models.DateTimeField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        'active_match',
        default=True
    )

    def __str__(self):
        return '{} - {}'.format(self.home_team, self.away_team)

