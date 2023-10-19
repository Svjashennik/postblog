import csv

from django.core.management import BaseCommand
from postblog.postblog.settings import BASE_DIR
from postblog.prediction.models import Book_tbl


class Command(BaseCommand):
    help = 'Set table data'

    def handle(self):
        with open(BASE_DIR + '/prediction/management/commands/books_data.csv') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for book in data:
                Book_tbl.objects.create(**book)

