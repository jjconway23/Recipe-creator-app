from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredients, Recipe

# ========================= List Views
def home(request):
    return render(request, 'create_meal/pages/index.html')


class IngredientsList(ListView):
    model = Ingredients
    template_name = 'create_meal/pages/ingredients_list.html'


class RecipeList(ListView):
    model = Recipe
    template_name = 'create_meal/pages/recipe_list.html'
    

    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        all_ingredients = Ingredients.objects.all()
        context["ingredients"] = all_ingredients
        return context

# ========================= Create Views

class IngredientsCreate(CreateView):
    model = Ingredients
    template_name = 'create_meal/pages/ingredients_create.html'
