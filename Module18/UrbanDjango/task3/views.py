from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView


def shop(request):
    title = 'Зоомагазин "Мир питомцев"'
    context = {
        'title': title,
    }
    return render(request, 'third_task/home_page.html', context)

def pets(request):
    title = 'Питомцы'
    pet1 = 'Попугай'
    pet2 = 'Хомяк'
    pet3 = 'Кролик'
    context = {
        'title': title,
        'pet1': pet1,
        'pet2': pet2,
        'pet3': pet3
    }
    return render(request, 'third_task/pets_page.html', context)

def basket(request):
    return render(request, 'third_task/basket_page.html')
