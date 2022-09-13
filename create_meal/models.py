from django.db import models

class Recipie(models.Model):
    name = models.CharField(max_length=30)
    cook_time = models.IntegerField()
    Ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)