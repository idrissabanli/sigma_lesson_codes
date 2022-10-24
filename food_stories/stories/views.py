from django.shortcuts import render
from django.shortcuts import get_object_or_404
from stories.models import (
    Recipe,
)


def recipe_list_page(request):
    recipes = Recipe.objects.all().order_by('-created_at', 'title')
    string  = 'Salam'
    
    context = {
        'recipe_list': recipes,
        'string': string
    }
    return render(request, 'recipes.html', context)

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', context)
