from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalCreateView,
)
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm
)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    resolved_url = resolve_url('/')
                    return HttpResponseRedirect(resolved_url)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    form = LoginForm()
    registration_url = resolve_url('/registration')
    return render(request, 'registration/login.html', {'form': form, 'registration_url': registration_url})

# для модального окна авторизации
class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "registration/login_form.html"
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('main')  # index


# не используется
def user_login_modal(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    resolved_url = resolve_url('/')
                    return HttpResponseRedirect(resolved_url)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    form = LoginForm()
    registration_url = resolve_url('/registration')
    return render(request, 'registration/login_form.html', {'form': form, 'registration_url': registration_url})


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            cd = form.cleaned_data
            new_user.set_password(cd['password'])
            new_user.save()
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    resolved_url = resolve_url('/')
                    return HttpResponseRedirect(resolved_url)
                else:
                    return HttpResponse('Disabled account')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

# для модального окна регистрации
class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup_form.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('main')


# не используется
def user_registration_modal(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            cd = form.cleaned_data
            new_user.set_password(cd['password'])
            new_user.save()
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    resolved_url = resolve_url('/')
                    return HttpResponseRedirect(resolved_url)
                else:
                    return HttpResponse('Disabled account')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup_form.html', {'form': form})
