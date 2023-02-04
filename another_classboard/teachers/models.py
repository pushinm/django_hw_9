from django.db import models
from .validators.validators import validate_age
from django.utils.crypto import get_random_string
import random
import string


# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    second_name = models.CharField(verbose_name='Фамилия', max_length=150)
    birth_day = models.DateField(verbose_name='Дата рождения', validators=[validate_age])
    email = models.EmailField(verbose_name='e-mail')
    phone = models.CharField(verbose_name='Телфон', max_length=11)
    login = models.CharField(verbose_name='Логин', max_length=15)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

        ordering = ['first_name', 'second_name']

    def __str__(self) -> str:
        return f'{self.first_name} {self.second_name}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('teachers:view_teacher', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.login == '':
            letters = string.ascii_lowercase
            rand_string = ''.join(random.choice(letters) for i in range(10))

            self.login = rand_string
            super(Teacher, self).save(*args, **kwargs)
