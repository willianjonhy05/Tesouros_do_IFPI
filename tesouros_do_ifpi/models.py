from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
import random
import uuid
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.

class Usuario(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    nome = models.CharField("Nome", max_length=100, blank=True, null=True)
    cpf = models.CharField("CPF", max_length=15, unique=True)
    telefone = models.CharField("Telefone", max_length=15, null=True, blank=True)
    data_nasc = models.DateField("Data de Nascimento", null=True, blank=True)
    matricula = models.CharField("Matrícula", max_length=20, null=True, blank=True)
    concorda_termos = models.BooleanField("Concorda com os termos", default=False)
    data_aceite = models.DateTimeField("Data de Aceite", null=True, blank=True)
    ip_aceite = models.GenericIPAddressField("IP de Aceite", null=True, blank=True)
    email = models.EmailField("Email", max_length=100, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def gerar_username(self):
        email = self.email
        if '@' in email:
            base_username = email.split('@')[0]
        else:
            base_username = email

        while True:
            numeros_aleatorios = ''.join(random.choices('0123456789', k=4))
            username = f"{base_username}{numeros_aleatorios}"
            if not Usuario.objects.filter(username=username).exists():
                break

        return username
    
    def gerar_senha_padrao(self):
        if self.cpf:
            return self.cpf.replace(".", "").replace("-", "")
        return None

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.gerar_username()
            
        if not self.password:
            senha_padrao = self.gerar_senha_padrao()
            if senha_padrao:
                self.set_password(senha_padrao)            
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.cpf
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"  
        
        
class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    descricao = models.TextField("Descrição", blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug and self.nome:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

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
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
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
    data_confirmacao = models.DateTimeField("Data de Confirmação", null=True, blank=True)
    confirmacao = models.BooleanField(default=False)
    
    def __str__(self):
       return f"Voto de {self.usuario.nome} em {self.categoria.nome}"
   
    class Meta:
        verbose_name = "Voto"
        verbose_name_plural = "Votos"
        unique_together = ['usuario', 'categoria']
        
        
class Foto(models.Model):
    nome = models.CharField("Nome", max_length=100)
    imagem = models.ImageField("Imagem", upload_to="fotos/fullsize/")
    imagem_thumb = models.ImageField(
        "Imagem (Thumbnail)",
        upload_to="fotos/thumbnails/",
        blank=True,
        null=True
    )
    descricao = models.TextField("Descrição", blank=True, null=True)
    link = models.URLField("Link", blank=True, null=True)
    ativo = models.BooleanField("Ativo", default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem and not self.imagem_thumb:
            self.gerar_thumbnail()

    def gerar_thumbnail(self):
        img = Image.open(self.imagem)

        # Converter se necessário
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        largura, altura = 650, 350

        img_ratio = img.width / img.height
        target_ratio = largura / altura

        # Crop proporcional
        if img_ratio > target_ratio:
            nova_largura = int(target_ratio * img.height)
            offset = (img.width - nova_largura) // 2
            img = img.crop((offset, 0, offset + nova_largura, img.height))
        else:
            nova_altura = int(img.width / target_ratio)
            offset = (img.height - nova_altura) // 2
            img = img.crop((0, offset, img.width, offset + nova_altura))

        img = img.resize((largura, altura), Image.LANCZOS)

        buffer = BytesIO()
        img.save(buffer, format="JPEG", quality=85)

        file_name = f"thumb_{self.pk}.jpg"

        self.imagem_thumb.save(
            file_name,
            ContentFile(buffer.getvalue()),
            save=False
        )

        super().save(update_fields=["imagem_thumb"])

    def __str__(self):
        return f"Foto: {self.nome}"

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"