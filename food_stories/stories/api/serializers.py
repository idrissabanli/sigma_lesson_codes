from rest_framework import serializers
from stories.models import Category, Recipe, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        fields = (
            'id',
            'title',
            'image',
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Tag
        fields = (
            'id',
            'title',
        )

class RecipeCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

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

    def validate(self, attr):
        request = self.context['request']
        attr['author'] = request.user
        return super().validate(attr)



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

