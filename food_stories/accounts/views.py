from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages

from accounts.forms import RegisterForm, LoginForm


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=False)
            return redirect(reverse_lazy('accounts:login'))
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('core:home'))
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request=request, username=form.cleaned_data['username'],
            password=form.cleaned_data['password'])
            if not user:
                messages.add_message(request, messages.ERROR, 'User not found!')
            django_login(request, user)
            return redirect(reverse_lazy('core:home'))
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('accounts:login'))
