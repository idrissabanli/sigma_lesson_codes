from django.shortcuts import render
from stories.models import (
    Recipe,
)


def recipe_list_page(request):
    recipes = Recipe.objects.all().order_by('-created_at', 'title')
    context = {
        'recipe_list': recipes
    }
    return render(request, 'recipes.html', context)