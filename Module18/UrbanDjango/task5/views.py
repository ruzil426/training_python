from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.

def sign_up_by_html(request):
    users = {'user': 'user', 'guest': 'guest', 'admin': 'admin'}
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        age = int(request.POST.get('age'))

        if password == password_repeat and age >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}')
        else:
            if password != password_repeat:
                info['error'] = 'Пароли не совпадают'
            if age < 18:
                info['error'] = 'Вы должны быть старше 18'
            if username in users:
                info['error'] = 'Пользователь уже существует'
    return render(request, 'fifth_task/registration_page.html', context=info)

def sign_up_by_django(request):
    users = {'user': 'user', 'guest': 'guest', 'admin': 'admin'}
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['password_repeat']
            age = int(form.cleaned_data['age'])

            if password == password_repeat and age >= 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}')
            elif password != password_repeat:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context=info)
