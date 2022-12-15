from django.urls import path
from core.views import (
    contact,
    home,
    ContactView,
    about,
)

app_name='core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    # path('contact/', contact, name='contact')
    path('contact/', ContactView.as_view(), name='contact'),
]
