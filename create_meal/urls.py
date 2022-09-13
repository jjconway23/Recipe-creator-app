from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('ingredients_list/', views.IngredientsList.as_view(), name='ingredients_list'),
    path('recipe_list/', views.RecipeList.as_view(), name='recipe_list'),
]