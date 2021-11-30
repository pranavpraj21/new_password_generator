from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(requests):
    return render(requests,'generator/home.html',{'random':777777})

def search(requests):
    return HttpResponse('<h1>Search option disabled</h1>')

def about(requests):
    return render(requests,'generator/about.html')

def password(requests):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length= int(requests.GET.get('length',12))
    if requests.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if requests.GET.get('Special'):
        characters.extend(list('!@#$%^&*()`~_-+={}:"<>?,./;''"`'))
    if requests.GET.get('Numbers'):
        characters.extend(list('1234567890'))
    result=''
    for i in range(length):
        result+=random.choice(characters)
    return render(requests,'generator/password.html',{'password':result})
