# Tesouros do IFPI

Plataforma web desenvolvida em **Django** para gerenciar o projeto **Tesouros do IFPI**, uma iniciativa de reconhecimento de alunos, ex-alunos, docentes, técnicos e colaboradores que se destacam em suas trajetórias e contribuições para a instituição.

O sistema permite autenticação de usuários, aceite de termos, registro de votos por categoria, gerenciamento administrativo, galeria de fotos do evento, envio de mensagens de contato e exportação de relatórios em Excel.

## Funcionalidades

- Página inicial institucional com apresentação do projeto
- Área de autenticação de usuários
- Controle de acesso com login obrigatório em áreas restritas
- Aceite de termos antes da votação
- Votação por categorias específicas
- Visualização dos votos do usuário autenticado
- Painel administrativo com estatísticas gerais
- Gerenciamento de categorias
- Gerenciamento de usuários
- Gerenciamento de fotos com ativação, edição e exclusão
- Formulário de contato
- Relatórios por categoria
- Exportação de votos confirmados em arquivo `.xlsx`
- Geração automática de thumbnails para imagens

## Tecnologias utilizadas

- Python 3
- Django 4.2
- PostgreSQL
- Gunicorn
- WhiteNoise
- Bootstrap 5
- OpenPyXL
- Pillow

## Dependências principais

```txt
asgiref==3.11.1
beautifulsoup4==4.14.3
dj-database-url==3.1.2
Django==4.2.29
django-bootstrap-v5==1.0.11
et_xmlfile==2.0.0
gunicorn==25.1.0
openpyxl==3.1.5
packaging==26.0
pillow==12.2.0
psycopg2-binary==2.9.11
python-decouple==3.8
soupsieve==2.8.3
sqlparse==0.5.5
typing_extensions==4.15.0
tzdata==2025.3
whitenoise==6.12.0
