from django.db import models


class Ingredient(models.Model):
    # Модель для ингредиентов
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Recipe(models.Model):
    # Модель для рецептов
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='recipes/images/', blank=True)
    description = models.TextField()
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
