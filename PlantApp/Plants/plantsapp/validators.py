from django.core.exceptions import ValidationError

def name_validator(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def letters_validator(value):
    for x in value:
        if not x.isalpha():
            raise ValidationError("Plant name should contain only letters!")


