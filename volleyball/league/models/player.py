""" Player Model """

# Django.
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from volleyball.utils.models import BaseModel

# Create your models here.


class Player(BaseModel):
    """
    Player model
    """

    person = models.ForeignKey(
        'league.Person',
        related_name='person',
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        'league.Team',
        related_name='team',
        on_delete=models.CASCADE
    )

    is_active = models.BooleanField(
        'active_player',
        default=True
    )

    def __str__(self):
        return '{} - {}'.format(self.person, self.team)