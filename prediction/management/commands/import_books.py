import csv

from django.core.management import BaseCommand
from postblog.settings import BASE_DIR
from prediction.models import Book_tbl


class Command(BaseCommand):
    help = 'Set table data'

    def handle(self, *args, **kwargs):
        with open(str(BASE_DIR) + '/prediction/management/commands/books_data.csv') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for book in data:
                for key, value in book.items():
                    if not value:
                        book[key] = None
                Book_tbl.objects.create(**book)

