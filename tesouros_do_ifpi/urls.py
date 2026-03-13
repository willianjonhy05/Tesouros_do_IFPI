from django.urls import path
from tesouros_do_ifpi import views

urlpatterns = [
    path('termos/', views.termos, name='termos'),
    path('votacao/', views.meus_votos, name='votacao'),
    path('processar/', views.processar_identificacao, name='processar_identificacao'),
    path('nao-autorizado/', views.nao_autorizado, name='nao_autorizado'),
    path('sair/', views.sair, name='sair'),
    path('home-contato/', views.home_contato, name='home_contato'),
    path('votar/<int:voto_id>/', views.votar, name='votar'),
    path("login/", views.login_view, name="login"),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('meus-votos/', views.meus_votos, name='meus_votos'),
]
