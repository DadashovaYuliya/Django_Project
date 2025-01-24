from django.shortcuts import render
from django.http import HttpResponse


def home_views(request):
    return render(request, 'home.html')


def contacts_views(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено. Ответ будет направлен по номеру: {phone}.')
    return render(request, 'contacts.html')
