from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url

from blogs.models import Post


def blog_view(request):
    if request.method == 'GET' and request.user.is_authenticated:
        posts = Post.objects.all().select_related('author')
        return render(request, 'blogs/main.html', {'posts': posts})
    else:
        resolved_url = resolve_url('/login/')
        return HttpResponseRedirect(resolved_url)
