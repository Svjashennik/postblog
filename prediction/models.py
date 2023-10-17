from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Book_tbl(models.Model):
    # id = models.BigIntegerField(null=False, blank=True)
    Edition = models.TextField(null=True, blank=True)
    Reviews = models.FloatField(null=True, blank=True)
    Ratings = models.BigIntegerField(null=True, blank=True)
    Edition_Year = models.BigIntegerField(null=True, blank=True)
    Price = models.FloatField(null=True, blank=True)

    # def __str__(self):
    #     return f'{self.title} {self.author.username}'

    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={"id": int(self.id)})


class Prediction_tbl(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pred')
    created_on = models.DateTimeField(default=timezone.now)
    # id = models.BigIntegerField(null=False, blank=True)
    Edition = models.TextField(null=True, blank=True)
    Reviews = models.FloatField(null=True, blank=True)
    Ratings = models.BigIntegerField(null=True, blank=True)
    Edition_Year = models.BigIntegerField(null=True, blank=True)
    Price = models.FloatField(null=True, blank=True)

    # def __str__(self):
    #     return f'{self.title} {self.author.username}'

    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={"id": int(self.id)})
