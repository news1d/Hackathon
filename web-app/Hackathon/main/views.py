from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'title': 'Генератор идей'})

def generate(request):
    return render(request, 'main/generate.html')

def add(request):
    return render(request, 'main/add.html')