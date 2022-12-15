from django.db import models
from django.urls  import reverse_lazy
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

    def __str__(self):
        return self.title


class Tag(AbstractModel):
    title = models.CharField(max_length=63)

    def __str__(self):
        return self.title


class Recipe(AbstractModel):
    '''
    This model for saving Recipe
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, )

    title = models.CharField(max_length=127)
    slug = models.SlugField(max_length=150)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/recipes')
    cover_image = models.ImageField(upload_to='media/recipes')

    def get_absolute_url(self):
        return reverse_lazy("stories:recipe_detail", kwargs={"pk": self.pk})

    # def save(self):
    #     self.slug = self.title + self.id
    #     super().save()

a = Recipe(title='lskdfndskl')

class Comment(AbstractModel):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

