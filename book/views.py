from django.shortcuts import render, redirect
from django.views.generic import View

from book.models import Book
from book.forms import BookForm


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
            return redirect(updated_book)

        return render(request, 'book/update.html', {'form': bound_form, 'book': book})
