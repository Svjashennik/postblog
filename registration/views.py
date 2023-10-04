from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm


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
