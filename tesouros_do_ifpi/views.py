from django.shortcuts import render, redirect
from .models import Contato, Usuario, Voto
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import ExAluno, AlunoAtual, DocenteAtual, ExDocente, TecnicoAdmAtual, ExTecnicoAdm, Terceirizado



FORM_CATEGORIAS = {

    "ex-aluno-do-ifpi": ExAluno,
    "aluno-atual-do-ifpi": AlunoAtual,
    "professor-atual-do-ifpi": DocenteAtual,
    "ex-professor-do-ifpi": ExDocente,
    "tecnico-atual-do-ifpi": TecnicoAdmAtual,
    "ex-tecnico-do-ifpi": ExTecnicoAdm,
    "terceirizado": Terceirizado,

}
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

def home_contato(request):

    if request.method == "POST":

        nome = request.POST.get("name")
        email = request.POST.get("email")
        telefone = request.POST.get("phone")        
        mensagem = request.POST.get("message")

        Contato.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,            
            mensagem=mensagem
        )

        messages.success(request, "Mensagem enviada com sucesso!")
        return redirect('index')

    return redirect('index')

def termos(request):

    if not request.session.get('cpf_autorizado'):
        return redirect('identificacao')
    
    if request.method == "POST":

        concorda_termos = request.POST.get('concorda_termos') == 'on'
        cpf = request.session.get('cpf_autorizado')

        if concorda_termos and cpf:

            usuario = get_object_or_404(Usuario, cpf=cpf)

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

    return render(request, 'meus_votos.html')

def identificacao(request):
    return render(request, 'identificacao.html')


def processar_identificacao(request):
    if request.method == "POST":
        cpf = request.POST.get('cpf')
        cpf = cpf.replace(".", "").replace("-", "")

        if Usuario.objects.filter(cpf=cpf).exists():
            request.session['cpf_autorizado'] = cpf
            
            usuario = get_object_or_404(Usuario, cpf=cpf)
            if usuario.concorda_termos:
                return redirect('votacao')
            else:
            
                return redirect('termos')
        else:
            return redirect('nao_autorizado')

    return redirect('identificacao')

def sair(request):
    request.session.flush()
    return redirect('identificacao')


def meus_votos(request):
    cpf = request.session.get('cpf_autorizado')

    if not cpf:
        return redirect('identificacao')

    usuario = get_object_or_404(Usuario, cpf=cpf)

    if usuario.concorda_termos == False:
        return redirect('termos')
    
    votos = Voto.objects.filter(usuario=usuario)

    return render(request, 'meus_votos.html', {'votos': votos})



def votar(request, voto_id):

    cpf = request.session.get('cpf_autorizado')

    if not cpf:
        return redirect('identificacao')

    usuario = get_object_or_404(Usuario, cpf=cpf)

    voto = get_object_or_404(Voto, id=voto_id, usuario=usuario)

    if voto.confirmacao:
        return redirect('votacao')

    FormClass = FORM_CATEGORIAS.get(voto.categoria.slug)

    if not FormClass:
        return redirect('votacao')

    if request.method == "POST":

        form = FormClass(request.POST, instance=voto)

        if form.is_valid():

            voto = form.save(commit=False)
            voto.confirmacao = True
            voto.data_confirmacao = timezone.now()
            voto.save()

            return redirect('votacao')

    else:

        form = FormClass(instance=voto)

    return render(request, "votar.html", {
        "form": form,
        "voto": voto
    })

def index(request):
    return render(request, 'index.html')


def nao_autorizado(request):
    return render(request, 'nao_autorizado.html')