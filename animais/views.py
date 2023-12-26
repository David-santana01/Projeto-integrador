from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.session.get('usuario'):
        return HttpResponse ('olá')
    else:
        return redirect('/auth/login/?status=2')
    