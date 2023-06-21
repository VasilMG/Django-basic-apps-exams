# Generated by Django 4.2.2 on 2023-06-18 15:46

import Plants.plantsapp.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14, verbose_name='Plant type')),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), Plants.plantsapp.validators.letters_validator])),
                ('image_url', models.URLField(verbose_name='URL Image')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[Plants.plantsapp.validators.name_validator])),
                ('last_name', models.CharField(max_length=20, validators=[Plants.plantsapp.validators.name_validator])),
                ('profile_picture', models.URLField(blank=True, null=True, verbose_name='Profile Picture')),
            ],
        ),
    ]