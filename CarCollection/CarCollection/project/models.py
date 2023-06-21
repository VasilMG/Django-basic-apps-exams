from django.db import models
from django.core.validators import MinLengthValidator

from CarCollection.project.validators import age_validator, year_validator


# Create your models here.

class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2),]
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=[age_validator,],
    )
    password = models.CharField(max_length=30)
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Car(models.Model):
    TYPES = (
        ("Sports Car", 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )

    car_type = models.CharField(
        max_length=10,
        choices=TYPES,
    )
    model = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2),],
    )
    year = models.IntegerField(
        validators=[year_validator,],
    )
    picture = models.URLField()
    price = models.FloatField()