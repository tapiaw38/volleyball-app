""" League Model """

# Django.
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from volleyball.utils.models import BaseModel

# Create your models here.


class League(BaseModel):
    """
    League model
    """

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    picture = models.ImageField(
        upload_to='league/',
        blank=True,
        null=True
    )

    teams = models.ManyToManyField(
        'league.Team',
        related_name='teams',
        through='league.TeamLeague',
        through_fields=('league', 'team')
    )

    is_active = models.BooleanField(
        'active_league',
        default=True
    )

    def __str__(self):
        return self.name