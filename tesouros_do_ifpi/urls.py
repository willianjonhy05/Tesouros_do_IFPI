from django.urls import path
from tesouros_do_ifpi import views

urlpatterns = [
    path('termos/', views.termos, name='termos'),
    path('votacao/', views.votacao, name='votacao'),
    path('processar/', views.processar_identificacao, name='processar_identificacao'),
    path('nao-autorizado/', views.nao_autorizado, name='nao_autorizado'),
    path('sair/', views.sair, name='sair'),
]
