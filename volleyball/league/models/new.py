""" New Model. """

# Django.
from django.db import models

# Utilities
from volleyball.utils.models import BaseModel


# Create your models here.


class New(BaseModel):
    """
    New Model.
    """

    title = models.CharField(
        'title',
        max_length=255
    )

    sub_title = models.CharField(
        'sub_title',
        max_length=255
    )

    content = models.TextField(
        'content'
    )

    league = models.ForeignKey(
        'league.League',
        related_name='league_new',
        on_delete=models.CASCADE
    )

    picture = models.ImageField(
        'picture',
        upload_to='league/new/',
        blank=True,
        null=True
    )

    def __str__(self):
        return '{} - {}'.format(self.league, self.title)
