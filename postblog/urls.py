from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from registration.views import user_login
from postblog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'login/', user_login, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
