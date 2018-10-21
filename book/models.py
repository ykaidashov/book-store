from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from stdnum import isbn, exceptions


def isbn_validator(raw_value):
    try:
        isbn.validate(raw_value)
    except exceptions.InvalidFormat as e:
        raise ValidationError(e.message)
    return True


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=14, validators=[isbn_validator])

    authors = models.ManyToManyField(Author, related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse('book_index_url')

    def get_update_url(self):
        return reverse('book_update_url', kwargs={'book_id': self.id})

    def __str__(self):
        return self.title
