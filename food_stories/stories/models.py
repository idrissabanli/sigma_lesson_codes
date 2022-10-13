from django.db import models
from django.contrib.auth import get_user_model
from core.models import AbstractModel

User = get_user_model()


class Category(AbstractModel):
    '''
    This model for saving Categories as Dessert, Food
    '''
    title = models.CharField(max_length=63)
    image = models.ImageField(upload_to='media/categories')
    # parent = models.ForeignKey('self ', on_delete=models.CASCADE)


class Tag(AbstractModel):
    title = models.CharField(max_length=63)


class Recipe(AbstractModel):
    '''
    This model for saving Recipe
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, )

    title = models.CharField(max_length=127)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/recipes')
    cover_image = models.ImageField(upload_to='media/recipes')


class Comment(AbstractModel):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
