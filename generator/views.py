from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepass = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list(map(str.upper,characters)))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+=<>,.?/;:[]{}\|`~'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))


    length = int(request.GET.get('length',12))

    for x in range(length):
        thepass += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepass})

def about(request):
    return render(request, 'generator/about.html')
