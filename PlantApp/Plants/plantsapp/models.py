from django.db import models
from django.core.validators import MinLengthValidator

from Plants.plantsapp.validators import name_validator, letters_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2),],
    )

    first_name = models.CharField(
        max_length=20,
        validators=[name_validator,]
    )

    last_name = models.CharField(
        max_length=20,
        validators=[name_validator,]
    )
    profile_picture = models.URLField(
        verbose_name="Profile Picture",
        blank=True,
        null=True,
    )


TYPES = (
    ("Outdoor Plants", "Outdoor Plants"),
    ("Indoor Plants", "Indoor Plants"),
)

class Plant(models.Model):
    plant_type = models.CharField(
        max_length=14,
        choices=TYPES,
        verbose_name= "Plant type"
    )
    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2), letters_validator],
    )
    image_url = models.URLField(
        verbose_name= "URL Image"
    )
    description = models.TextField()
    price = models.FloatField()
