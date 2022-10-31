from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from core.forms import (
    ContactForm,
)


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutt.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form =  ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Tesdiqlendi!!')
            return redirect(reverse_lazy('core:home'))
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
