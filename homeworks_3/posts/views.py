from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {
        "title": "Главная страница",
        "my_list": [1, 2, 3, 4, 5],
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        "title": "О нас",
    }
    return render(request, "about.html", context)


def contact(request):
    context = {
        "title": "Контакты",
    }
    return render(request, "contacts.html", context)