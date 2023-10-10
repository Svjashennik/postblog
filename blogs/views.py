import time

from deep_translator import GoogleTranslator
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from google_trans_new import google_translator

from blogs.models import Post


def blog_view(request, page=1):
    if request.method == 'GET' and request.user.is_authenticated:
        posts = Post.objects.all().select_related('author').order_by('title')
        lang = request.GET.get('lang')
        paginator = Paginator(posts, per_page=5)
        page_object = paginator.get_page(page)
        if lang == 'en':
            blog_translate = GoogleTranslator(source='ru', target='en')
            for post in page_object:
                time.sleep(0.5)
                post.body = blog_translate.translate(post.body)
        context = {"page_obj": page_object, 'current_page': page, 'lang': 'en' if lang == 'ru' else 'ru'}
        return render(request, 'blogs/main.html', context)
    else:
        resolved_url = resolve_url('/login/')
        return HttpResponseRedirect(resolved_url)
