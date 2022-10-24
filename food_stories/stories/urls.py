from django.urls import path
from stories.views import (
    recipe_list_page,
    recipe_detail
)

app_name='stories'

urlpatterns = [
    path('recipes/', recipe_list_page, name='recipes_page'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe_detail'),
]
