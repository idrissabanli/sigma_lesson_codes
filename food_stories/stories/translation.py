from modeltranslation.translator import translator, TranslationOptions
from stories.models import Recipe


class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'short_description', 'description')


translator.register(Recipe, RecipeTranslationOptions)