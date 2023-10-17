from django.core.management import BaseCommand

from blogs.models import Post
from data import fixtures


class Command(BaseCommand):
    help = 'Fill database'

    def handle(self, *args, **kwargs):
        if Post.objects.all().count() < 2:
            for post in fixtures:
                Post.objects.create(**post)
