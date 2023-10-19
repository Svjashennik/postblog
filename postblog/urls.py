from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from registration.views import (
    user_login,
    user_registration,
    CustomLoginView,
    SignUpView,
    user_login_modal,
    user_registration_modal,
)
from postblog import settings
from blogs.views import blog_view, post_detail, post_about, post_login_dialog
from prediction.views import post_result, post_prediction, show_books_tbl, show_prediction_tbl, learn_model

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', user_login, name='login'),
    path('login_dialog/', post_login_dialog, name='login_dialog'),
    path('login_modal/', CustomLoginView.as_view(), name='login_modal'),
    # path('login_modal/', user_login_modal, name='login_modal'),
    path('signup_modal/', SignUpView.as_view(), name='signup_modal'),
    # path('signup_modal/', user_registration_modal, name='signup_modal'),
    path('registration/', user_registration, name='registration'),
    #   path('translate/', blog_translate, name='translate'),
    path('', blog_view, name='main'),
    path('<int:page>/', blog_view, name='main_pagination'),
    path("detail<int:id>/", post_detail, name="post_detail"),
    path('about/', post_about, name='about'),
    path('prediction/', post_prediction, name='prediction'),
    path('result*/', post_result, name='result'),
    path('booklist/', show_books_tbl, name='booklist'),
    path('prediction_list/', show_prediction_tbl, name='prediction_list'),
    path('learn_model/', learn_model, name='learn_model'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
