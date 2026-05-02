# DevLAb Ronilson

Projeto Django desenvolvido como prática acadêmica para gestão de eventos, usuários, equipes e projetos.

A aplicação reúne uma API back-end com Django e Django REST Framework, estrutura modular por apps e páginas/templates para apoio ao fluxo do sistema.

## Objetivo

Construir uma base de sistema web para organizar informações acadêmicas e administrativas, com entidades separadas por domínio e possibilidade de evolução para uma API REST completa.

## Funcionalidades

- Cadastro e organização de usuários.
- Cadastro e organização de equipes.
- Cadastro e organização de projetos.
- Estrutura Django separada em apps.
- Templates e arquivos estáticos para interface web.
- Base preparada para rotas e integrações com Django REST Framework.

## Tecnologias

- Python 3
- Django 5
- Django REST Framework
- SQLite em desenvolvimento
- HTML, CSS e templates Django

## Como Rodar

Clone o repositório:

```bash
git clone https://github.com/csantos18/DevLAb-Ronilson.git
cd DevLAb-Ronilson
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

## Estrutura

```text
.
├── api_equipes/      # App de equipes
├── api_projetos/     # App de projetos
├── api_usuarios/     # App de usuários
├── devlab/           # Configuração principal do Django
├── static/           # Arquivos estáticos
├── templates/        # Templates HTML
├── manage.py
├── requirements.txt
└── README.md
```

## Boas Práticas

- Use ambiente virtual local (`.venv/`) em vez de versionar dependências instaladas.
- Não publique `db.sqlite3`, arquivos `.env`, logs ou caches Python.
- Atualize o `requirements.txt` quando adicionar dependências.

## Status

Projeto acadêmico em evolução.
