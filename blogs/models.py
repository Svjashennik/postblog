from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    title = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} {self.author.username}'
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"id": int(self.id)})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
