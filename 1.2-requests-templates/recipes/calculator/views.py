from django.shortcuts import render
from django.http import HttpResponse
import copy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

result = copy.deepcopy(DATA)

def get_serv(request):
    try:
        servings = int(request.GET.get("servings", 1))
    except ValueError:
        servings = 1 
    return servings

def omelet(request):
    servings = get_serv(request)
    for k, v in DATA["omlet"].items():
        result["omlet"][k] = round(v * servings, 2)
    context = {"recipe": result["omlet"]}
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = get_serv(request)
    for k, v in DATA["pasta"].items():
        result["pasta"][k] = round(v * servings, 2)
    context = {"recipe": result["pasta"]}
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = get_serv(request)
    for k, v in DATA["buter"].items():
        result["buter"][k] = round(v * servings, 2)
    context = {"recipe": result["buter"]}
    return render(request, 'calculator/index.html', context)
