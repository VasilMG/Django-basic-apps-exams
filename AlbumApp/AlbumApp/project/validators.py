from django.core.exceptions import ValidationError


def username_validator(value):
    for x in value:
        if not x.isalpha() and x != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
    return value

def below_zero_validator(value):
    if value < 0:
        raise ValidationError("The value cannot be below zero.")
    return value