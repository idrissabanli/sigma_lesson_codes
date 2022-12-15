from django.urls import path
from stories.views import (
    recipe_list_page,
    like_post,
    RecipeListView, 
    RecipeDetailView,
    RecipeUpdateView
)

app_name='stories'

urlpatterns = [
    # path('recipes/', recipe_list_page, name='recipes_page'),
    path('recipes/', RecipeListView.as_view(), name='recipes_page'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/<int:pk>/update', RecipeUpdateView.as_view(), name='recipe_update'),
    path('like-post/<int:pk>/', like_post, name='like_post'),
]
