from django.db import models


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
    isbn = models.CharField(max_length=13)

    authors = models.ManyToManyField(Author)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
