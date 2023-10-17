from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} {self.author.username}'

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": int(self.id)})

