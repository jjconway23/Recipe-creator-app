from django.db import models
from django.contrib.auth.models import User

class Ingredients(models.Model):
    GRAMS = 'G'
    MILLILITRES = 'ML'
    TABLESPOON = 'TBSP'
    TEASPOON = 'TSP'
    UNIT_CHOICES = [
        (GRAMS, 'Grams'),
        (MILLILITRES, 'Millilitres'),
        (TABLESPOON, 'Tablespoon'),
        (TEASPOON, 'Teaspoon'),
    ]
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=40)
    unit = models.CharField(max_length=4, choices=UNIT_CHOICES, null=True, blank=True, default="")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=30)
    cook_time = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredients)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='recipies')


    def __str__(self):
        return self.name
