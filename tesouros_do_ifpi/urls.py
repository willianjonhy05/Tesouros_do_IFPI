from django.urls import path
from tesouros_do_ifpi import views

urlpatterns = [
    path('termos/', views.termos, name='termos'),
    path('votacao/', views.meus_votos, name='votacao'),
    # path('processar/', views.processar_identificacao, name='processar_identificacao'),
    path('nao-autorizado/', views.nao_autorizado, name='nao_autorizado'),
    path('sair/', views.sair, name='sair'),
    path('home-contato/', views.home_contato, name='home_contato'),
    # path('votar/<int:voto_id>/', views.votar, name='votar'),
    path('votar/<uuid:uuid>/', views.votar, name='votar'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('categorias/', views.listar_categorias, name='categorias'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('contatos/', views.listar_contatos, name='contatos'),
    path('votos/', views.listar_votos, name='indicacoes'),
    path('votos/relatorio/<slug:slug>/', views.relatorio_categoria, name='relatorio_categoria'),
    path('votos/relatorio/<slug:slug>/excel/', views.exportar_excel_categoria, name='exportar_excel_categoria'),
    path('fotos/', views.listar_fotos, name='fotos'),
    path('fotos/criar/', views.criar_foto, name='criar_foto'),
    path('fotos/editar/<int:id>/', views.editar_foto, name='editar_foto'),
    path('fotos/toggle/<int:id>/', views.toggle_foto, name='toggle_foto'),
    path('fotos/excluir/<int:id>/', views.excluir_foto, name='excluir_foto'),
    path('usuarios/', views.listar_usuarios, name='usuarios'),
    path('usuarios/criar/', views.criar_usuario, name='criar_usuario'),
    path('usuarios/apagar/<int:id>/', views.apagar_usuario, name='apagar_usuario'),
    # path('meus-votos/', views.meus_votos, name='meus_votos'),
]
