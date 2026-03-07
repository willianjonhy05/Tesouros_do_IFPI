from django.shortcuts import render, redirect
from .models import Contato, Usuario
from django.contrib import messages
from django.utils import timezone

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

    if not request.session.get('cpf_autorizado'):
        return redirect('identificacao')

    if request.method == "POST":

        concorda_termos = request.POST.get('concorda_termos') == 'on'
        cpf = request.session.get('cpf_autorizado')

        if concorda_termos and cpf:

            usuario = Usuario.objects.get_or_create(cpf=cpf)

            usuario.concorda_termos = True
            usuario.data_aceite = timezone.now()

            ip = request.META.get('REMOTE_ADDR')
            usuario.ip_aceite = ip

            usuario.save()

            return redirect('votacao')

        else:
            messages.error(request, "Você deve concordar com os termos para continuar.")
            return redirect('termos')

    return render(request, 'termos.html')

def votacao(request):

    cpf = request.session.get('cpf_autorizado')

    if not cpf:
        return redirect('identificacao')

    usuario = Usuario.objects.filter(cpf=cpf, concorda_termos=True).first()

    if not usuario:
        return redirect('termos')

    return render(request, 'votacao.html')

def identificacao(request):
    return render(request, 'identificacao.html')


def processar_identificacao(request):
    if request.method == "POST":
        cpf = request.POST.get('cpf')
        cpf = cpf.replace(".", "").replace("-", "")

        if Usuario.objects.filter(cpf=cpf).exists():
            request.session['cpf_autorizado'] = cpf
            return redirect('termos')
        else:
            return redirect('nao_autorizado')

    return redirect('identificacao')

def sair(request):
    request.session.flush()
    return redirect('identificacao')


def index(request):
    return render(request, 'index.html')


def nao_autorizado(request):
    return render(request, 'nao_autorizado.html')