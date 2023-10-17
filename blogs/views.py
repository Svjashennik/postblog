import time

from deep_translator import GoogleTranslator
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url, get_object_or_404
from django.views.generic import ListView, DetailView

from blogs.models import Post


def blog_view(request, page=1):
    if request.method == 'GET' and request.user.is_authenticated:
        posts = Post.objects.all().select_related('author').order_by('title')
        lang = request.GET.get('lang', 'ru')
        paginator = Paginator(posts, per_page=2)
        page_object = paginator.get_page(page)
        if lang == 'en':
            blog_translate = GoogleTranslator(source='ru', target='en')
            for post in page_object:
                time.sleep(0.5)
                post.body = blog_translate.translate(post.body)
                post.title = blog_translate.translate(post.title)
        context = {"page_obj": page_object, 'current_page': page, 'lang': 'en' if lang == 'ru' else 'ru'}
        return render(request, 'blogs/main.html', context)
    else:
        resolved_url = resolve_url('/login_dialog/')
        return HttpResponseRedirect(resolved_url)


def post_detail(request, id):
    template_name = "blogs/post_detail.html"
    post = get_object_or_404(Post, pk=id)
    return render(
        request,
        template_name,
        {
            "post": post,
        },
    )


def post_about(request):
    template_name = 'about.html'
    return render(request, template_name)


def post_login_dialog(request):
    template_name = 'registration/login_dialog.html'
    return render(request, template_name)
