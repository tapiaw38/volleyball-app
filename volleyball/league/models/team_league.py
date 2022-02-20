""" Team League Model """

# Django.
from django.db import models

# Utilities
from volleyball.utils.models import BaseModel

# Create your models here.


class  TeamLeague(BaseModel):
    """
    Team League model
    """

    league = models.ForeignKey(
        'league.League',
        related_name='league_team',
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        'league.Team',
        related_name='team_league',
        on_delete=models.CASCADE
    )

    points = models.IntegerField(
        default=0
    )

    matches_played = models.IntegerField(
        default=0
    )

    is_active = models.BooleanField(
        'active_team_league',
        default=True
    )

    def __str__(self):
        return '{} - {}'.format(self.league, self.team)