from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientsForm, RecipeForm
from .models import Ingredients, Recipe
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


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
    form_class = IngredientsForm

    def get_success_url(self):
        return '/ingredients_list/'



class RecipeCreate(CreateView):
    model = Recipe
    template_name = 'create_meal/pages/recipe_create.html'
    form_class = RecipeForm

    def get_success_url(self):
        return '/recipe_list/'


# ========================= Update Views


class IngredientsUpdate(UpdateView):
    model = Ingredients
    template_name = 'create_meal/pages/ingredients_update.html'
    fields = '__all__'

    def get_success_url(self):
        return '/ingredients_list/'


class RecipeUpdate(UpdateView):
    model = Recipe
    template_name = 'create_meal/pages/recipe_update.html'
    fields = '__all__'

    def get_success_url(self):
        return '/recipe_list/'


# ========================= Delete Views


class IngredientsDelete(DeleteView):
    model = Ingredients
    template_name = 'create_meal/pages/ingredients_delete.html'
    
    def get_success_url(self):
        return '/ingredients_list/'


class RecipeDelete(DeleteView):
    model = Recipe
    template_name = 'create_meal/pages/recipe_delete.html'
    
    def get_success_url(self):
        return '/recipe_list/'

# ========================= Registration Views

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("invalid credentials")
    return render(request, "create_meal/pages/registration/login.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "create_meal/pages/registration/signup.html"


def logout_view(request):
    logout(request)
    return redirect("home")