from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ingredients, Recipe

class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

