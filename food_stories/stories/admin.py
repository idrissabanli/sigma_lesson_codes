from django.contrib import admin
from stories.models import Comment, Recipe, Category, Tag
from modeltranslation.admin import TranslationAdmin


admin.site.register([Comment, Category, Tag])


class CommentAdminInline(admin.TabularInline):
    model = Comment


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     pass


@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    inlines = (CommentAdminInline,)
    list_display = (
        'id',
        'title', 
        'category',
        'created_at',
    )
    list_filter = (
        'category__title',
    )
    search_fields = (
        'title',
        'category__title',
        'author__username'
    )
