from django.forms import ModelForm
from django import forms
from .models import Ingredients, Recipe

class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name', 'quantity', 'unit']


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'cook_time', 'ingredients']

