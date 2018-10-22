import logging

from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from book.models import Book
from book.forms import BookForm

logger = logging.getLogger('book')


def index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books': books})


class BookCreate(View):

    def get(self, request):
        form = BookForm()
        return render(request, 'book/create.html', {'form': form})

    def post(self, request):
        bound_form = BookForm(request.POST)

        if bound_form.is_valid():
            book = bound_form.save()
            logger.info(f'Create new book: {book.title}')
            return redirect(book)

        return render(request, 'book/create.html', {'form': bound_form})


class BookUpdate(View):

    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        bound_form = BookForm(instance=book)
        return render(request, 'book/update.html', {'form': bound_form, 'book': book})

    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        bound_form = BookForm(request.POST, instance=book)

        if bound_form.is_valid():
            updated_book = bound_form.save()
            logger.info(f'Update book: {updated_book.title}')
            return redirect(updated_book)

        return render(request, 'book/update.html', {'form': bound_form, 'book': book})


class BookDelete(View):

    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        return render(request, 'book/delete.html', {'book': book})

    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        book.delete()
        logger.info(f'Delete book: {book.title}')
        return redirect(reverse('book_index_url'))
