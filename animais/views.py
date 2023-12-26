from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Animais

# Create your views here.

def home(request):
    pets = Animais.objects.all( )
    return render(request,'home.html', {'Pets': pets})