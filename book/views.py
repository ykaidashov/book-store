from django.shortcuts import render

from book.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books': books})
