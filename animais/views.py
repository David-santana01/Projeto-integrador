from django.shortcuts import render,redirect
from django.http import HttpResponse
from usuario.models import usuario

# Create your views here.

def home(request):
    if request.session.get('usuario'):
        Usuario = usuario.objects.get(id = request.session['Usuario']) .nome
        return render(request, 'home.html')
    
    else:
        return redirect('/auth/login/?status=2')
    