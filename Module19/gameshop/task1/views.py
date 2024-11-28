from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


def shop(request):
    title = 'Магазин "Мир игр"'
    context = {
        'title': title,
    }
    return render(request, 'home_page.html', context)

def games(request):
    title = 'Игры'
    all_games = Game.objects.all()
    context = {
        'title': title,
        'all_games': all_games
    }
    return render(request, 'games_page.html', context)

def basket(request):
    title = 'Ваша корзина'
    context = {'title': title}
    return render(request, 'basket_page.html', context)

# def sign_up_by_html(request):
#     users = {'user': 'user', 'guest': 'guest', 'admin': 'admin'}
#     info = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         password_repeat = request.POST.get('password_repeat')
#         age = int(request.POST.get('age'))
#
#         if password == password_repeat and age >= 18 and username not in users:
#             return HttpResponse(f'Приветствуем, {username}')
#         else:
#             if password != password_repeat:
#                 info['error'] = 'Пароли не совпадают'
#             if age < 18:
#                 info['error'] = 'Вы должны быть старше 18'
#             if username in users:
#                 info['error'] = 'Пользователь уже существует'
#     return render(request, 'registration_page.html', context=info)

def sign_up_by_django(request):
    buyers = Buyer.objects.all()
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['password_repeat']
            age = int(form.cleaned_data['age'])

            existing_buyer = Buyer.objects.filter(name=username).first()
            #print(existing_buyer)
            if password == password_repeat and age >= 18:
                if existing_buyer is None:
                    Buyer.objects.create(name=username, balance='100', age=age)
                    return HttpResponse(f'Приветствуем, {username}')
                else:
                    info['error'] = 'Пользователь уже существует'
            elif password != password_repeat:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', context=info)