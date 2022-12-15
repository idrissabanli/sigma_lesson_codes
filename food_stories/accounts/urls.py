from django.urls import path, re_path
from accounts.views import (
    register, logout, user_profile, activate, UserLoginView, LoginView, UserPasswordChangeView,
    UserPasswordResetView, UserPasswordRestDoneView,
    UserPasswordResetConfirmView
)
from django.contrib.auth.views import PasswordChangeView


app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('user-profile/', user_profile, name='user_profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password-change'),
    path('password-reset/', UserPasswordResetView.as_view(), name='password-reset'),
    path('logout/', logout, name='logout'),
    path('password-reset-done/', UserPasswordRestDoneView.as_view(), name='password-reset-done'),
    re_path(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$', 
            UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        activate, name='activate'),
]