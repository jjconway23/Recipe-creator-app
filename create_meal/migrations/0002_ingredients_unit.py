# Generated by Django 3.2.15 on 2022-09-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_meal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='unit',
            field=models.CharField(choices=[('G', 'Grams'), ('ML', 'Millilitres'), ('TBSP', 'Tablespoon'), ('TSP', 'Teaspoon')], max_length=4, null=True),
        ),
    ]