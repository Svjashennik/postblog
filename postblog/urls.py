from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from registration.views import user_login, user_registration
from postblog import settings
from blogs.views import blog_view, post_detail, post_about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('registration/', user_registration, name='registration'),
    #   path('translate/', blog_translate, name='translate'),
    path('', blog_view, name='main'),
    path('<int:page>/', blog_view, name='main_pagination'),
    path("detail<int:id>/", post_detail, name="post_detail"),
    path('about/', post_about, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
