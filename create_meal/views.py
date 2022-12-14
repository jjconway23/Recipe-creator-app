from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import IngredientsForm, RecipeForm
from .models import Ingredients, Recipe



# ========================= List Views
def home(request):
    return render(request, 'create_meal/pages/index.html')


class IngredientsList(LoginRequiredMixin, ListView):
    model = Ingredients
    template_name = 'create_meal/pages/ingredients_list.html'
    redirect_field_name = 'login'
    login_url = 'login'


class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'create_meal/pages/recipe_list.html'
    

    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        all_ingredients = Ingredients.objects.all()
        context["ingredients"] = all_ingredients
        return context

# ========================= Create Views

class IngredientsCreate(LoginRequiredMixin, CreateView):
    model = Ingredients
    template_name = 'create_meal/pages/ingredients_create.html'
    form_class = IngredientsForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return '/ingredients_list/'



class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'create_meal/pages/recipe_create.html'
    form_class = RecipeForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return '/recipe_list/'


# ========================= Update Views


class IngredientsUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredients
    template_name = 'create_meal/pages/ingredients_update.html'
    fields = '__all__'

    def get_success_url(self):
        return '/ingredients_list/'


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = 'create_meal/pages/recipe_update.html'
    fields = '__all__'

    def get_success_url(self):
        return '/recipe_list/'


# ========================= Delete Views


class IngredientsDelete(LoginRequiredMixin, DeleteView):
    model = Ingredients
    template_name = 'create_meal/pages/ingredients_delete.html'
    
    def get_success_url(self):
        return '/ingredients_list/'


class RecipeDelete(LoginRequiredMixin, DeleteView):
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
            return redirect("ingredients_list")
        else:
            return HttpResponse("invalid credentials")
    return render(request, "create_meal/pages/registration/login.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "create_meal/pages/registration/signup.html"

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


