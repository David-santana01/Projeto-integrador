from .models import usuario
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from hashlib import sha256
# Create your views here.

def login(request):
    status = request.GET.get('status')
    return render(request,'login.html', {'status': status})

def cadastro (request):
    status = request.GET.get('status')
    return render(request,'cadastro.html', {'status': status})

def validar_cadastro(request,):
    Nome = request.POST.get('nome')
    Senha = request.POST.get('senha')
    Email = request.POST.get('email')

    Usuario = usuario.objects.filter(email = Email)
     
     #Essa parte do codigo era pra ser integrada com o html para aparecer as notificações mas não esta
     #funcionando direito ainda não achei o erro 
    
    if len(Nome.strip()) == 0 or len(Email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(Senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(Usuario) > 0:
        return redirect('/auth/cadatro/?status=3')

    try:
        Senha = sha256(Senha.encode()).hexdigest()
        Usuario = usuario(nome = Nome,
                          senha = Senha,
                          email = Email)
        Usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')


def validar_login(request):
    Email = request.POST.get('email')
    Senha = request.POST.get('senha')
    Senha = sha256(Senha.encode()).hexdigest()
    Usuario = usuario.objects.filter(email = Email).filter(senha = Senha)
    if len(Usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(Usuario) > 0:
       request.session['Usuario'] = Usuario[0].id
       return redirect(f'/animais/home') 
    
    return HttpResponse(f"{Email} {Senha}")

def sair(request):
    request.session.flush()
    return redirect('/auth/login/')