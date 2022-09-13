from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()



class Recipe(models.Model):
    name = models.CharField(max_length=30)
    cook_time = models.IntegerField()
    Ingredients = models.ManyToManyField(Ingredients)

