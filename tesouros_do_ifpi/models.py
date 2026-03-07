from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField("Nome", max_length=100, blank=True, null=True)
    cpf = models.CharField("CPF", max_length=15, null=True, blank=True)
    telefone = models.CharField("Telefone", max_length=15, null=True, blank=True)
    data_nasc = models.DateField("Data de Nascimento", null=True, blank=True)
    matricula = models.CharField("Matrícula", max_length=20, null=True, blank=True)
    concorda_termos = models.BooleanField("Concorda com os termos", default=False)
    data_aceite = models.DateTimeField("Data de Aceite", null=True, blank=True)
    ip_aceite = models.GenericIPAddressField("IP de Aceite", null=True, blank=True)
    email = models.EmailField("Email", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.cpf
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"  
        
        
class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=100, blank=True, null=True)
    descricao = models.TextField("Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"        


class Contato(models.Model):
    
    ASSUNTO_CHOICES = [
        ("critica", "Crítica"),
        ("sugestao", "Sugestão"),
        ("duvida", "Dúvida"),
        ("erro", "Erro"),
        ("outros", "Outros"),
    ]
        
    nome = models.CharField("Nome", max_length=100, blank=True, null=True)
    email = models.EmailField("Email", max_length=100, blank=True, null=True)
    assunto = models.CharField("Assunto", max_length=20, choices=ASSUNTO_CHOICES, blank=True, null=True)
    telefone = models.CharField("Telefone", max_length=15, null=True, blank=True)
    mensagem = models.TextField("Mensagem", blank=True, null=True)
    data = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        
        
class Voto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField("Nome do indicado", max_length=200, blank=True, null=True)
    nome_curso = models.CharField("Nome do Curso", max_length=200, blank=True, null=True)
    nome_departamento = models.CharField("Nome do Departamento", max_length=200, blank=True, null=True)
    nome_funcao = models.CharField("Nome da Função", max_length=200, blank=True, null=True)
    nome_setor = models.CharField("Nome do Setor", max_length=200, blank=True, null=True)
    nome_empresa = models.CharField("Nome da Empresa", max_length=200, blank=True, null=True)
    nome_ou_ocupacao_atual = models.CharField("Função/Ocupação Atual", max_length=200, blank=True, null=True)
    data_voto = models.DateTimeField(auto_now_add=True)
    confirmacao = models.BooleanField(default=False)
    
    def __str__(self):
       return f"Voto de {self.usuario.nome} em {self.categoria.nome}"
   
    class Meta:
        verbose_name = "Voto"
        verbose_name_plural = "Votos"