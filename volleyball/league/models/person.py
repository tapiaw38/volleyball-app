""" Person Model """

# Django.
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from volleyball.utils.models import BaseModel

# Create your models here.


class Person(BaseModel):
    """
    Person Model
    """

    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    document_regex = RegexValidator(
        regex=r'\d{8,8}$',
        message="You must enter a DNI number without points."
    )

    document = models.CharField(
        validators=[document_regex], 
        max_length=8,
        unique=True,
        blank=True,
        null=True
    )

    phone_regex = RegexValidator(
        regex=r'\d{10,10}$',
        message= "You must enter a number with the following format: 3837430000. Up to 10 digits."
    )

    phone_number = models.CharField(
        validators=[phone_regex], 
        max_length=10, 
        blank=True, 
        null=True 
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        'active_Person',
        default=True
    )

    def __str__(self):
        return self.name