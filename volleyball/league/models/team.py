""" Team Model """

# Django.
from django.db import models

# Utilities.
from volleyball.utils.models import BaseModel

# Create your models here.

class Team(BaseModel):
    """
    Team model.
    """
    
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    picture = models.ImageField(
        upload_to='team/',
        blank=True,
        null=True
    )

    players = models.ManyToManyField(
        'league.Person',
        related_name='players',
        through='league.Player',
        through_fields=('team', 'person')
    )

    is_active = models.BooleanField(
        'active_team',
        default=True
    )

    def __str__(self):
        return self.name