[![Build Status](https://travis-ci.com/ffabiorj/relatorio_app.svg?branch=master)](https://travis-ci.com/ffabiorj/voluntario_app)

[![codecov](https://codecov.io/gh/ffabiorj/relatorio_app/branch/master/graph/badge.svg)](https://codecov.io/gh/ffabiorj/voluntario_app)

# Criação de um app de relatório

## Link do projeto em produção

[Relatorio APP](https://relatorio-app.herokuapp.com/)

## Ferramentas

- Django
- Postgres

### Obs:

No frontend eu utilizei CDN do Bootstrap porque é um projeto simples.

## Roda o projeto localmente:

1. Clone o repositório.
2. Entre na pasta.
3. Crie uma um ambiente de desenvolvimento com python 3.8.
4. Ative o ambiente.
5. Instale as dependências.
6. Crie um arquivo .env
7. Rode as migrações
8. Rode o script para popular o BD
9. Rode o projeto
10. Acesse o link

```
- git clone git@github.com:ffabiorj/relatorio_app.git
- cd relatorio_app
- python3 -m venv .venv
- source .venv/bin/activate
- pip install -r requirements-dev.txt
- python contrib/env_gen.py
- python manage.py migrate
- python import_data.py
- python manage.py runserver
- http://127.0.0.1:8000/
```

### Rodar os testes

```
pytest
```

### Links para as ferramentas utilizadas

[Django](https://docs.djangoproject.com/)

[Postgres](https://www.postgresql.org/)

[Codecov](https://codecov.io/)

[Travis](https://travis-ci.com/)
