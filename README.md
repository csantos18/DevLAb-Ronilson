# DevLAb Ronilson

Projeto Django desenvolvido como prática acadêmica no **Instituto Federal de Brasília (IFB), Campus Gama**, em Brasília-DF.

A aplicação reúne uma base web com Django e Django REST Framework, organizada em apps para usuários, equipes e projetos. O foco do repositório é demonstrar evolução em back-end, estruturação de projeto, documentação e boas práticas de versionamento.

## Contexto Acadêmico

Este projeto faz parte de atividades de estudo e participação acadêmica no **IFB Campus Gama**, unidade do Instituto Federal de Brasília localizada na região administrativa do Gama, em Brasília-DF. Ele não deve ser lido como produto final de produção, mas como registro prático de aprendizado em desenvolvimento web com Python e Django.

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

Configure as variáveis de ambiente com base em `.env.example`:

```text
DJANGO_SECRET_KEY=troque-esta-chave-em-producao
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_CORS_ALLOW_ALL_ORIGINS=True
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

## Qualidade e Segurança

Com as dependências instaladas, valide o projeto com:

```bash
python manage.py check
```

Para uma checagem mais próxima de produção:

```powershell
$env:DJANGO_DEBUG="False"
$env:DJANGO_SECRET_KEY="uma-chave-segura-com-mais-de-cinquenta-caracteres-para-teste"
$env:DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost"
$env:DJANGO_CORS_ALLOW_ALL_ORIGINS="False"
$env:DJANGO_SECURE_SSL_REDIRECT="True"
python manage.py check --deploy
```

O projeto usa configurações por variável de ambiente para evitar segredo fixo no código e facilitar deploy em ambientes diferentes.

## Boas Práticas

- Use ambiente virtual local (`.venv/`) em vez de versionar dependências instaladas.
- Não publique `db.sqlite3`, arquivos `.env`, logs ou caches Python.
- Atualize o `requirements.txt` quando adicionar dependências.
- Em produção, defina `DJANGO_DEBUG=False`, configure `DJANGO_ALLOWED_HOSTS` e use uma `DJANGO_SECRET_KEY` forte.
- Libere CORS apenas para origens conhecidas usando `DJANGO_CORS_ALLOWED_ORIGINS`.

## Status

Projeto acadêmico em evolução.
