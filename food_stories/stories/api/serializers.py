from rest_framework import serializers
from stories.models import Category, Recipe

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        fields = (
            'id',
            'title',
            'image',
        )

class RecipeCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'author',
            'category',
            'tags',
            'title',
            'slug',
            'short_description',
            'description',
            'image',
            'cover_image',
            'created_at',
            'updated_at',
        )


class RecipeSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.title')
    category = CategorySerializer()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'author',
            'category',
            'tags',
            'title',
            'slug',
            'short_description',
            'description',
            'image',
            'cover_image',
            'created_at',
            'updated_at',
        )

