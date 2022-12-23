from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages, auth
from django.core.validators import validate_email

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def register(request: HttpRequest):

    if request.method != 'POST':
        return render(request, 'account/register.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    confirma_senha = request.POST.get('confirma_senha')

    if not nome or not sobrenome or not email or not usuario or not senha or not confirma_senha:
        messages.add_message(request, messages.ERROR, 'Adicione todos os campos')
        return render(request, 'account/register.html')
    
    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.ERROR, 'Email Inválido')
        return render(request, 'account/register.html')
    
    if senha != confirma_senha:
        messages.add_message(request, messages.ERROR, 'Senhas não coincidem.')
        return render(request, 'account/register.html')
    
    if senha != confirma_senha:
        messages.add_message(request, messages.ERROR, 'Senhas não coincidem.')
        return render(request, 'account/register.html')
    
    if User.objects.filter(username=usuario).exists(): # Ele checa se ja exite esse usuario no banco
        messages.add_message(request, messages.ERROR, 'Usuário já existe')
        return render(request, 'account/register.html')

    if User.objects.filter(email=email).exists(): # Ele checa se ja exite esse usuario no banco
        messages.add_message(request, messages.ERROR, 'Email já existe')
        return render(request, 'account/register.html')

    user =  User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)

    user.save()
    
    return redirect('login')


def login(request: HttpRequest):
    if request.method != 'POST':
        return render(request, 'account/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')


    if not usuario or not senha:
        messages.add_message(request, messages.ERROR, 'Preencha todos os campos')
        return render(request, 'account/login.html')
    
    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.add_message(request, messages.ERROR, 'Usuário ou senha incorretos')
        return render(request, 'account/login.html')
    else:
        auth.login(request, user)
        return redirect('dashboard')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'account/dashboard.html')