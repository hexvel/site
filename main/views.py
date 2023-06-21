from django.shortcuts import render
from .models import User


def main_page(request):
    users = User.objects.all()
    return render(request, 'main/index.html', {'title': "Главная", 'users': users})

def about_us(request):
    return render(request, 'main/about.html')

def authorize(request):
    return render(request, 'main/auth.html')