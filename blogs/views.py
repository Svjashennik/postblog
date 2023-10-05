from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url

from blogs.models import Post


def blog_view(request, page=1):
    if request.method == 'GET' and request.user.is_authenticated:
        posts = Post.objects.all().select_related('author').order_by('title')
        paginator = Paginator(posts, per_page=5)
        page_object = paginator.get_page(page)
        context = {"page_obj": page_object}
        return render(request, 'blogs/main.html', context)
    else:
        resolved_url = resolve_url('/login/')
        return HttpResponseRedirect(resolved_url)
