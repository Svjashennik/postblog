from django.contrib import admin
from blogs.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    search_fields = ['title']
    list_select_related = ['author']
