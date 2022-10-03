from django.contrib import admin
from stories.models import Comment, Recipe, Category, Tag


admin.site.register([Comment, Recipe, Category, Tag])
