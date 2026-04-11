# import os
# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
# django.setup()

# from tesouros_do_ifpi.models import Categoria

# categorias = [
#     ("Ex-Aluno", "Posição no Mercado de Trabalho; Reconhecimento Social."),
#     ("Aluno Atual", "Desempenho no Curso; Participação em Eventos e Pesquisas; Estar no último período do Curso."),
#     ("Ex-Professor", "Ações que lhe deram destaque na trajetória da Instituição; Dinâmica de Ensino memorável."),
#     ("Professor Atual", "Ações Inovadoras; Participação em Projetos e Extensão."),
#     ("Ex-Técnico", "Proatividade; Marcas das suas ações na história da Instituição."),
#     ("Técnico Atual", "Proatividade; Empatia."),
#     ("Terceirizado", "Eficiência; Socialização."),
# ]

# for nome, descricao in categorias:
#     Categoria.objects.get_or_create(
#         nome=nome,
#         defaults={"descricao": descricao}
#     )

# print("Categorias criadas com sucesso!")

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from tesouros_do_ifpi.models import Categoria
from tesouros_do_ifpi.models import Usuario

categorias = [
    ("Ex-Aluno", "Posição no Mercado de Trabalho; Reconhecimento Social.", "ex-aluno-do-ifpi"),
    ("Aluno Atual", "Desempenho no Curso; Participação em Eventos e Pesquisas; Estar no último período do Curso.", "aluno-atual-do-ifpi"),
    ("Ex-Professor", "Ações que lhe deram destaque na trajetória da Instituição; Dinâmica de Ensino memorável.", "ex-professor-do-ifpi"),
    ("Professor Atual", "Ações Inovadoras; Participação em Projetos e Extensão.", "professor-atual-do-ifpi"),
    ("Ex-Técnico", "Proatividade; Marcas das suas ações na história da Instituição.", "ex-tecnico-do-ifpi"),
    ("Técnico Atual", "Proatividade; Empatia.", "tecnico-atual-do-ifpi"),
    ("Terceirizado", "Eficiência; Socialização.", "terceirizado-do-ifpi"),
]

for nome, descricao, slug in categorias:
    Categoria.objects.get_or_create(
        slug=slug,  # importante usar slug como identificador único
        defaults={
            "nome": nome,
            "descricao": descricao
        }
    )

print("Categorias criadas com sucesso!")


alunos_teste = [
    {
        "nome": "João Silva",
        "cpf": "973.201.473-35",
        "telefone": "(99) 99999-9999",
        "data_nasc": "1995-01-01",
        "matricula": "20210001",
        "email": "joao.silva@example.com"
    },
    {
        "nome": "Maria Oliveira",
        "cpf": "131.587.942-50",
        "telefone": "(88) 88888-8888",
        "data_nasc": "1996-02-02",
        "matricula": "20210002",
        "email": "maria.oliveira@example.com"
    }

]

for aluno in alunos_teste:
    Usuario.objects.get_or_create(
        email=aluno["email"],
        defaults={
            "nome": aluno["nome"],
            "cpf": aluno["cpf"],
            "telefone": aluno["telefone"],
            "data_nasc": aluno["data_nasc"],
            "matricula": aluno["matricula"],
            "concorda_termos": False,
        }
    )
    
print("Alunos de teste criados com sucesso!")