from .models import Voto
from django.forms import ModelForm
from django import forms


class BaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control"
            })


class ExAluno(BaseForm):
    class Meta:
        model = Voto
        fields = ['nome', 'nome_curso', 'nome_ou_ocupacao_atual']    
        labels = {
            'nome': 'Nome do ex-aluno',
            'nome_curso': 'Curso realizado no IFPI',
            'nome_ou_ocupacao_atual': 'Profissão ou ocupação atual',
        }
        
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do ex-aluno'}),
            'nome_curso': forms.TextInput(attrs={'placeholder': 'Digite o curso realizado no IFPI'}),
            'nome_ou_ocupacao_atual': forms.TextInput(attrs={'placeholder': 'Digite a profissão ou ocupação atual'}),
        }
        

class AlunoAtual(BaseForm):
    class Meta:
        model = Voto
        fields = ['nome', 'nome_curso']    
        labels = {
            'nome': 'Nome do aluno',
            'nome_curso': 'Curso/Módulo realizado no IFPI',
        }
        
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do aluno'}),
            'nome_curso': forms.TextInput(attrs={'placeholder': 'Digite o curso/módulo realizado no IFPI'}),
        }
        
class DocenteAtual(BaseForm):
    class Meta:
        model = Voto
        fields = ['nome', 'nome_curso']    
        labels = {
            'nome': 'Nome do docente',
            'nome_curso': 'Curso/Disciplina que leciona no IFPI',
        }
        
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do docente'}),            
            'nome_curso': forms.TextInput(attrs={'placeholder': 'Digite o curso/disciplina que leciona no IFPI'}),
        }

class ExDocente(BaseForm):
    class Meta:
        model = Voto
        fields = ['nome', 'nome_curso', 'nome_ou_ocupacao_atual']    
        labels = {
            'nome': 'Nome do docente',
            'nome_curso': 'Curso/Disciplina que lecionou no IFPI',
            'nome_ou_ocupacao_atual': 'Profissão ou ocupação atual',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do docente'}),            
            'nome_curso': forms.TextInput(attrs={'placeholder': 'Digite o curso/disciplina que lecionou no IFPI'}),
            'nome_ou_ocupacao_atual': forms.TextInput(attrs={'placeholder': 'Digite a profissão ou ocupação atual'}),
        }
        
class TecnicoAdmAtual(BaseForm):
    class Meta:
        model = Voto
        fields = ['nome', 'nome_setor', 'nome_funcao']    
        labels = {
            'nome': 'Nome do Técnico-administrativo',
            'nome_funcao': 'Função que exerce no IFPI',
            'nome_setor': 'Setor onde atua no IFPI',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do técnico-administrativo'}),
            'nome_funcao': forms.TextInput(attrs={'placeholder': 'Digite a função que exerce no IFPI'}),
            'nome_setor': forms.TextInput(attrs={'placeholder': 'Digite o setor onde atua no IFPI'}),
        }
        
class ExTecnicoAdm(BaseForm):
    class Meta:
        model = Voto
        fields = ['nome', 'nome_setor', 'nome_funcao', 'nome_ou_ocupacao_atual']    
        labels = {
            'nome': 'Nome do Técnico-administrativo',
            'nome_funcao': 'Função que exerceu no IFPI',
            'nome_setor': 'Setor onde atuou no IFPI',
            'nome_ou_ocupacao_atual': 'Profissão ou ocupação atual',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do técnico-administrativo'}),
            'nome_funcao': forms.TextInput(attrs={'placeholder': 'Digite a função que exerceu no IFPI'}),
            'nome_setor': forms.TextInput(attrs={'placeholder': 'Digite o setor onde atuou no IFPI'}),
            'nome_ou_ocupacao_atual': forms.TextInput(attrs={'placeholder': 'Digite a profissão ou ocupação atual'}),
        }
        
class Terceirizado(BaseForm):
    class Meta:
        model = Voto
        fields = ['nome', 'nome_funcao', 'nome_setor' ,'nome_empresa']    
        labels = {
            'nome': 'Nome do terceirizado',
            'nome_funcao': 'Função que exerce no IFPI',
            'nome_setor': 'Setor onde atua no IFPI',
            'nome_empresa': 'Empresa Terceirizada onde trabalha',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do terceirizado'}),
            'nome_funcao': forms.TextInput(attrs={'placeholder': 'Digite a função que exerce no IFPI'}),
            'nome_setor': forms.TextInput(attrs={'placeholder': 'Digite o setor onde atua no IFPI'}),
            'nome_empresa': forms.TextInput(attrs={'placeholder': 'Digite a empresa terceirizada onde trabalha'}),
        }