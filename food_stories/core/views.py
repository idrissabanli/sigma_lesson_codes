from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from core.models import Contact
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


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('core:home')
    # http_method_names = ('get',)

    # def get_success_url(self):
    #     messages.add_message(self.request, messages.SUCCESS, 'Tesdiqlendi!!')
    #     return super().get_success_url()

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Tesdiqlendi!!')
        return super().form_valid(form)



