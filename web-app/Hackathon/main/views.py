from django.shortcuts import render, HttpResponse
from .models import ideas
import sqlite3
import random

from distutils.log import debug


def index(request):
    return render(request, 'main/index.html', {'title': 'Генератор идей'})

def generate(request):
   if request.method == 'POST':
       gen_idea = ideas.objects.order_by('?')[:1]
       print(gen_idea)
   else:
       gen_idea = {'Сам хз как эта строчка работает, но на ней весь код держится)))'}
   return render(request, 'main/generate.html', {'gen_idea': gen_idea})

def add(request):
    if request.method == 'POST':
        idea = request.POST['idea']
        print(idea)
        obj = ideas()
        obj.idea = idea
        obj.save()
    context = {

    }
    return render(request, 'main/add.html', context)
