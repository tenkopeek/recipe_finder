from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count, F, Q

from .models import Ingredient, Recipe


def index(request):
    # Перенаправление с корневого URL на /home/ (старый адрес).
    return redirect('home')


def home(request):
    """Главная страница поиска.

    - Показывает все ингредиенты списком чекбоксов.
    - Если выбран хотя бы один ингредиент, ищет рецепты, которые полностью уместятся в выбранных ингредиентах.
    """

    selected_ids = request.GET.getlist('ingredients')
    ingredients = Ingredient.objects.order_by('name')

    recipes = []
    if selected_ids:
        # Жёсткое соответствие: рецепт должен содержать только выбранные ингредиенты.
        recipes = Recipe.objects.annotate(
            total_ingredients=Count('ingredients'),
            matches=Count('ingredients', filter=Q(ingredients__id__in=selected_ids)),
        ).filter(total_ingredients=F('matches'))

    return render(request, 'recipe_finder/home.html', {
        'ingredients': ingredients,
        'selected_ids': list(map(int, selected_ids)) if selected_ids else [],
        'recipes': recipes,
    })


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_finder/recipe_detail.html', {'recipe': recipe})
