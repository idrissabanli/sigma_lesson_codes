from django.urls import path
from stories.api.views import categories, RecipeAPIView, RecipeRetrieveUpdateDestroyAPIView, TagListAPIView


urlpatterns = [
    path('categories/', categories, name='categories'),
    path('tags/', TagListAPIView.as_view(), name='tags'),
    path('recipes/', RecipeAPIView.as_view(), name='recipes'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroyAPIView.as_view(), name='recipe_read_update_delete'),
    path('categories/<int:pk>/', categories, name='categories')
]