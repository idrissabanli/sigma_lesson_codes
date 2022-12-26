# from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from stories.models import Category, Recipe
from stories.api.serializers import (
    CategorySerializer, RecipeSerializer,
    RecipeCreateSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

def categories(request):
    category_list = Category.objects.all()
    serializer = CategorySerializer(category_list, many=True)
    # category_dict_list = []
    # for cat in category_list:
    #     category_dict_list.append({
    #         'id': cat.id,
    #         'title': cat.title,
    #         'image': cat.image.url
    #     })
    return JsonResponse(data=serializer.data, safe=False)


class RecipeAPIView(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return RecipeCreateSerializer
        return RecipeSerializer


class RecipeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RecipeSerializer
        return super().get_serializer_class()

    


# @api_view(http_method_names=['GET', 'POST'])
# def recipes(request):
#     if request.method == 'POST':
#         data = {}
#         # data.update(**request.POST)
#         # data.update(**request.FILES)
#         # print(data)
#         serializer = RecipeCreateSerializer(data=request.data, context={'request': request},)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, safe=False, status=201)
#         else:
#             return JsonResponse(data=serializer.errors, safe=False, status=400)
#     recipe_list = Recipe.objects.all()
#     serializer  = RecipeSerializer(recipe_list, context={'request': request}, many=True)
#     return JsonResponse(data=serializer.data, safe=False)


# @api_view(http_method_names=['PUT', 'PATCH'])
# def recipe_read_update_delete(request, pk):
#     if request.method == 'PUT':
#         recipe = Recipe.objects.get(id=pk)
#         serializer = RecipeCreateSerializer(data=request.data, instance=recipe, context={'request': request},)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, safe=False, status=200)
#         else:
#             return JsonResponse(data=serializer.errors, safe=False, status=400)
#     if request.method == 'PATCH':
#         recipe = Recipe.objects.get(id=pk)
#         serializer = RecipeCreateSerializer(data=request.data, instance=recipe, partial=True, context={'request': request},)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, safe=False, status=200)
#         else:
#             return JsonResponse(data=serializer.errors, safe=False, status=400)
