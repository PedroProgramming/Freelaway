from django.shortcuts import render, redirect
from .utils import validar_campos
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login as logar, logout


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'login.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')

        if not validar_campos(username, senha):
            messages.add_message(request, constants.ERROR, 'Campos inválidos')
            return redirect('/auth/login/')

        usuario = authenticate(username=username, password=senha)
        
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/auth/login')
        else:
            logar(request, usuario)
            return redirect('/jobs/encontrar_jobs/')


def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if not validar_campos(username, password, confirm_password):
            messages.add_message(request, constants.ERROR, 'Campos inválidos')
            return redirect('/auth/cadastro/')

        if not password == confirm_password:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/cadastro/')
        
        user = User.objects.filter(username = username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse username')
            return redirect('/auth/cadastro/')
        
        try: 
            user = User.objects.create_user(
                username=username,
                password=password,
            )

            user.save()

            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
            return redirect('/auth/login/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        

def sair(request):
    logout(request)
    return redirect('/auth/login/')
