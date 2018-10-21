from django.core.management.base import BaseCommand, color_style

from book.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--order', default='asc', type=str, choices=['asc', 'desc'], dest='order')

    def handle(self, *args, **options):
        order = options['order']
        order_by = {
            'asc': 'publish_date',
            'desc': '-publish_date'
        }
        books = Book.objects.order_by(order_by[order])

        line = f'{"=" * 20} Books {"=" * 20}'

        self.stdout.write(self.style.SUCCESS(line))

        for book in books:
            authors = ', '.join([author.full_name for author in book.authors.all()])
            data = {
                'title': book.title,
                'isbn': book.isbn,
                'authors': authors,
                'price': book.price,
                'publish_date': book.publish_date
            }

            t = 'Title: {title} ISBN: {isbn} Authors: {authors} Price: {price}$ Publish date: {publish_date}'.format(
                **data)
            self.stdout.write(t)

        self.stdout.write(self.style.SUCCESS("=" * len(line)))
