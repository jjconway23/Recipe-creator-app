from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('ingredients_list/', views.IngredientsList.as_view(), name='ingredients_list'),
    path('recipe_list/', views.RecipeList.as_view(), name='recipe_list'),
    path('ingredients_list/create/', views.IngredientsCreate.as_view(), name='ingredients_create'),
    path('recipe_list/create'/ views.RecipeCreate.as_view(), name='recipe_create'),
]