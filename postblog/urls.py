from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from registration.views import user_login, user_registration
from postblog import settings
from blogs.views import blog_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('registration/', user_registration, name='registration'),
    path('', blog_view, name='main'),
    path('<int:page>/', blog_view, name='main_pagination'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
