from django.core.validators import MinLengthValidator
from django.db import models

from AlbumApp.project.validators import username_validator, below_zero_validator


# Create your models here.

class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[username_validator, MinLengthValidator(2),]
    )
    email = models.EmailField()

    age = models.IntegerField(
        validators=[below_zero_validator,],
        blank=True,
        null=True,
    )


class Album(models.Model):
    GENRES = (("Pop Music", "Pop Music"),
              ("Jazz Music", "Jazz Music"),
              ("R&B Music", "R&B Music"),
              ("Rock Music", "Rock Music"),
              ("Country Music", "Country Music"),
              ("Dance Music", "Dance Music"),
              ("Hip Hop Music", "Hip Hop Music"),
              ("Other", "Other"),
              )
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name= "Album name",
    )
    artist = models.CharField(
        max_length=30,
    )
    genre = models.CharField(
        max_length=30,
        choices=GENRES,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        verbose_name="Image URL",
    )
    price = models.FloatField(
        validators=[below_zero_validator, ],
    )