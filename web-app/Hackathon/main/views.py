from django.shortcuts import render, HttpResponse
from .models import ideas
import sqlite3
import random

from distutils.log import debug

def get_idea():
    try:
        con = sqlite3.connect('C:/Users/ARTEM/Desktop/Hackathon-develop_max/web-app/Hackathon/db_of_ideas.db')
        cursor = con.cursor()
    except Exception as ex:
        print("db is not exist")
        exit(1)
    max_id = cursor.execute("""SELECT id FROM ideas ORDER BY id DESC LIMIT 1""").fetchone()
    return cursor.execute("""SELECT idea FROM ideas WHERE id = ?""",(random.randint(1,max_id[0]),)).fetchone()

def insert_idea(idea):
    try:
        con = sqlite3.connect('C:/Users/ARTEM/Desktop/Hackathon-develop_max/web-app/Hackathon/db_of_ideas.db')
        cursor = con.cursor()
    except Exception as ex:
        print("db is not exist")
        exit(1)
    cursor.execute("""INSERT INTO ideas(idea) VALUES (?)""",(idea,)) #idea должен быть string
    con.commit()



def index(request):
    return render(request, 'main/index.html', {'title': 'Генератор идей'})

def generate(request):
   if request.method == 'POST':
       gen_idea = ideas.objects.order_by('?')[:1]
       # gen_idea = get_idea()
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
        #insert_idea(idea)
    context = {

    }
    return render(request, 'main/add.html', context)
