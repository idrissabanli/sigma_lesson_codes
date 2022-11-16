from django.urls import path, re_path
from accounts.views import register, login, logout, user_profile, activate

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('user-profile/', user_profile, name='user_profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        activate, name='activate'),
]