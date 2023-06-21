from django.core.exceptions import ValidationError


def age_validator(value):
    if value < 18:
        raise ValidationError("Age must be above 18")
    return value

def year_validator(value):
    if value < 1980 or value > 2049:
        raise ValidationError('Year must be between 1980 and 2049')
    return value

def price_validator(value):
    if value < 1:
        raise ValidationError("Price cannot be below 1")
    return value