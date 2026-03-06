from django.shortcuts import render, redirect
from .models import Contato
from django.contrib import messages

# Create your views here.


# def contato(request):
#     return render(request, 'contato.html')

def contato(request):
    if request.method == "POST":
        # Captura os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')
        
        # Cria um novo contato no banco de dados
        contato = Contato(nome=nome, email=email, assunto=assunto, telefone=telefone, mensagem=mensagem)
        contato.save()

        # Mensagem de sucesso
        messages.success(request, "Mensagem enviada com sucesso!")
        
        # Redireciona para a mesma página ou para uma página de sucesso
        return redirect('contato')  # Aqui, você pode mudar o redirecionamento para outra página de sucesso

    return render(request, 'contato.html')

def termos(request):
    return render(request, 'termos.html')

def votacao(request):
    return render(request, 'votacao.html')

def index(request):
    return render(request, 'index.html')