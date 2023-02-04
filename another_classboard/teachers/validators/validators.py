from datetime import date
from django.core.exceptions import ValidationError


def validate_age(value):
    days_in_year = 365.2425
    age = int((date.today() - value).days / days_in_year)
    if age < 18:
        raise ValidationError('Вам должно быть от 18 лет.')