from django.forms import ModelForm
from .models import Ingredients, Recipe


class IngredientsForm(ModelForm):
    model = Ingredients
    fields = '__all__'