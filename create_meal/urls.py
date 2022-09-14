from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingredients_list/', views.IngredientsList.as_view(), name='ingredients_list'),
    path('recipe_list/', views.RecipeList.as_view(), name='recipe_list'),
    path('ingredients_list/create/', views.IngredientsCreate.as_view(), name='ingredients_create'),
    path('recipe_list/create', views.RecipeCreate.as_view(), name='recipe_create'),
    path('ingredients_list/update/<pk>/', views.IngredientsUpdate.as_view(), name='ingredients_update'),
    path('recipe_list/update/<pk>/', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('ingredients_list/delete/<pk>', views.IngredientsDelete.as_view(), name='ingredients_delete'),
    path('recipe_list/delete/<pk>', views.RecipeDelete.as_view(), name='recipe_delete'),
    path('login/', views.login_page, name='login'),
    path('signup/',views.SignUp.as_view(), name='signup'),

]
