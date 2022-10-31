import datetime
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from stories.models import (
    Recipe,
)


def recipe_list_page(request):
    recipes = Recipe.objects.all().order_by('-created_at', 'title')
    string  = 'Salam'
    print('liked_posts', request.session.get('liked_posts', ''))
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


# def like_post(request, pk):
#     messages.add_message(request, messages.SUCCESS, 'Beyenildi')
#     request.session['liked_posts'] = request.session.get('liked_posts', '') + str(pk)+' '
#     return render(request, 'recipes.html')

def like_post(request, pk):
    response = HttpResponse('blah')
    max_age = 30 * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', '') + str(pk)+' ', expires=expires)
    return response
