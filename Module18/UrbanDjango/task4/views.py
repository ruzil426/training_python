from django.shortcuts import render
from django.views.generic import TemplateView


def shop(request):
    title = 'Зоомагазин "Мир питомцев"'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/home_page.html', context)

def pets(request):
    title = 'Питомцы'
    pet1 = 'Попугай'
    pet2 = 'Хомяк'
    pet3 = 'Кролик'
    pets = ['Попугай', 'Хомяк', 'Кролик', 'Рыбки']
    context = {
        'title': title,
        # 'pet1': pet1,
        # 'pet2': pet2,
        # 'pet3': pet3
        'pets': pets
    }
    return render(request, 'fourth_task/pets_page.html', context)

def basket(request):
    title = 'Ваша корзина'
    context = {'title': title}
    return render(request, 'fourth_task/basket_page.html', context)
