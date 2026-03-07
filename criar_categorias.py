import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from tesouros_do_ifpi.models import Categoria

categorias = [
    ("Ex-Aluno", "Posição no Mercado de Trabalho; Reconhecimento Social."),
    ("Aluno Atual", "Desempenho no Curso; Participação em Eventos e Pesquisas; Estar no último período do Curso."),
    ("Ex-Professor", "Ações que lhe deram destaque na trajetória da Instituição; Dinâmica de Ensino memorável."),
    ("Professor Atual", "Ações Inovadoras; Participação em Projetos e Extensão."),
    ("Ex-Técnico", "Proatividade; Marcas das suas ações na história da Instituição."),
    ("Técnico Atual", "Proatividade; Empatia."),
    ("Terceirizado", "Eficiência; Socialização."),
]

for nome, descricao in categorias:
    Categoria.objects.get_or_create(
        nome=nome,
        defaults={"descricao": descricao}
    )

print("Categorias criadas com sucesso!")