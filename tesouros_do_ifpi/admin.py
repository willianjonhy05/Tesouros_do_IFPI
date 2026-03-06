from django.contrib import admin
from .models import Usuario, Contato, Categoria, Voto

# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nome","email", "telefone", "cpf"]
    search_fields = ["cpf"]
    list_per_page = 10
    
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ["nome", "email", "assunto", "data"]
    search_fields = ["email", "assunto"]
    list_per_page = 10
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nome", "descricao"]
    search_fields = ["nome"]
    list_per_page = 10
    
@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ["usuario", "categoria", "data_voto"]
    search_fields = ["usuario__nome", "categoria__nome"]
    list_per_page = 10