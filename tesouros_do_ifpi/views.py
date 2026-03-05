from django.shortcuts import render

# Create your views here.


def contato(request):
    return render(request, 'contato.html')

def termos(request):
    return render(request, 'termos.html')

def votacao(request):
    return render(request, 'votacao.html')