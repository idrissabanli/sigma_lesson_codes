from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.views.generic import TemplateView

from stories.models import Recipe
from accounts.tokens import account_activation_token
from accounts.forms import (
    RegisterForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm,
    UserSetPasswordForm
)
from accounts.tasks import send_confirmation_mail

User = get_user_model()


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            current_site = get_current_site(request)
            send_confirmation_mail(user, current_site)
            return redirect(reverse_lazy('accounts:login'))
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

# def login(request):
#     next_page = request.GET.get('next', reverse_lazy('core:home'))
#     if request.user.is_authenticated:
#         return redirect(reverse_lazy('core:home'))
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = authenticate(request=request, username=form.cleaned_data['username'],
#             password=form.cleaned_data['password'])
#             if user:
#                 django_login(request, user)
#                 return redirect(next_page)
#             messages.add_message(request, messages.ERROR, 'User not found!')
#     context = {
#         'form': form
#     }
#     return render(request, 'login.html', context)

class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = False

    # def dispatch(self, request, )


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('accounts:login'))

@login_required
def user_profile(request):
    return render(request, 'user-profile.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Account activated')
        return redirect(reverse_lazy('accounts:login'))
    else:
        messages.add_message(request, messages.ERROR, 'Account not activated')
        return redirect(reverse_lazy('core:home'))



class UserPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        django_logout(self.request)
        return super().form_valid(form)


class UserPasswordResetView(PasswordResetView):
    template_name = 'reset_password.html'
    form_class = UserPasswordResetForm
    email_template_name = 'password-reset-email.html'
    success_url = reverse_lazy('accounts:password-reset-done')


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'confirm_password.html'
    form_class = UserSetPasswordForm
    success_url = reverse_lazy('accounts:password-reset-done')


class UserPasswordRestDoneView(TemplateView):
    template_name = 'password_reset_done.html'
