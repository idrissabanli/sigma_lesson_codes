import datetime
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from stories.forms import CommentForm, RecipeForm

from stories.models import (
    Recipe,
    Category,
    Tag
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


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    context_object_name = 'recipes'
    ordering = ('-created_at',)
    paginate_by = 1


# def recipe_detail(request, pk):
#     recipe = get_object_or_404(Recipe, pk=pk)
#     context = {
#         'recipe': recipe
#     }
#     return render(request, 'recipe_detail.html', context)


class RecipeDetailView(FormMixin, DetailView):
    form_class = CommentForm
    model = Recipe
    template_name = 'recipe_detail.html'

    def get_success_url(self):
        return reverse_lazy("stories:recipe_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#       context = {
# #         'recipe': recipe
# #     }
        categories = Category.objects.all()
        context['categories'] = categories
        context["form"] = self.get_form()
#       context = {
#         'recipe': recipe
#         'categories': categories
#         'form': CommentForm
#     }
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.recipe = self.get_object()
        form.instance.user =  self.request.user
        form.save()
        return super().form_valid(form)


class RecipeUpdateView(UpdateView):
    template_name = 'update_recipe.html'
    form_class = RecipeForm
    # success_url = 
    model = Recipe

    # def form_valid(self, form):
    #     tag_list = form.cleaned_data['tag_list'].split()
    #     tags = list(filter(lambda word: word.startswith('#'), tag_list))
    #     recipe = self.get_object()
    #     recipe.tags.through.objects.all().delete()
    #     result = super().form_valid(form)
    #     for tag in tags:
    #         tag_object, created = Tag.objects.get_or_create(title=tag[1:])
    #         # recipe.tags.set([tag_object])
    #         # a = recipe.tags.through.objects.create(tag_id=tag_object.id, recipe_id=recipe.id)
    #         # print(a)
    #         recipe.tags.add(tag_object)
    #     recipe.save()
    #     return result

#     def form_valid(form):
#         recipe = form.save(commit=False)
#         recipe.save()
#         form.save_m2m()
#         return super().form_valid()

    # def get_success_url(self):
    #     return reverse_lazy("stories:recipe_detail", kwargs={"pk": self.object.pk})

    


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
