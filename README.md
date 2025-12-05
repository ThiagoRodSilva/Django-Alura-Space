# Django Alura Space
Este é o projeto "Django Alura Space", um aplicativo web desenvolvido com Django durante os cursos da Alura. O objetivo é gerenciar e compartilhar conteúdos, como imagens e posts, para usuários de uma comunidade ou espaço, aplicando os principais conceitos e práticas do framework Django.

## Vitrine.Dev - Informações para a Alura
✨ Thiago, Django Alura Space
🏷️ Tecnologias, Django, Python, Bootstrap, SQLite, Amazon S3
URL, [Insira aqui a URL do seu deploy (Ex: Render, Heroku)]
Desafio, [Insira aqui a URL do desafio/curso da Alura, se aplicável]
[https://i.imgur.com/exemplo-capa-django.png#vitrinedev] 
---

## Funcionalidades

*   Cadastro e autenticação de usuários
*   Upload e gerenciamento de imagens/posts
*   Visualização de posts públicos ou privados
*   Interface amigável construída com Bootstrap
*   Restrição de acesso a conteúdos conforme perfil do usuário

## Tecnologias utilizadas

*   Python 3.14
*   Django
*   Bootstrap
*   SQLite (padrão do Django, fácil de trocar por outro banco)
*   Amazon S3

## Como rodar o projeto

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/Thiago4596/Django-Alura-Space.git](https://github.com/Thiago4596/Django-Alura-Space.git)
    ```
2.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Prepare o banco de dados**
    ```bash
    python manage.py migrate
    ```
4.  **Crie um usuário administrador**
    ```bash
    python manage.py createsuperuser
    ```
5.  **Inicie o servidor de desenvolvimento**
    ```bash
    python manage.py runserver
    ```
6.  Acesse `http://localhost:8000` no navegador para usar a aplicação.

## Estrutura do projeto
Com certeza! Vou adaptar o seu README.md para incluir o cabeçalho específico do vtrine.dev e garantir que ele seja reconhecido e exibido corretamente na sua Vitrine.

Aqui está o README.md formatado, com um link de imagem de capa de exemplo incluído no padrão #vitrinedev.

Markdown

# Django Alura Space
Este é o projeto "Django Alura Space", um aplicativo web desenvolvido com Django durante os cursos da Alura. O objetivo é gerenciar e compartilhar conteúdos, como imagens e posts, para usuários de uma comunidade ou espaço, aplicando os principais conceitos e práticas do framework Django.

## Vitrine.Dev - Informações para a Alura
✨ Thiago, Django Alura Space
🏷️ Tecnologias, Django, Python, Bootstrap, SQLite, Amazon S3
URL, [Insira aqui a URL do seu deploy (Ex: Render, Heroku)]
Desafio, [Insira aqui a URL do desafio/curso da Alura, se aplicável]
[https://i.imgur.com/exemplo-capa-django.png#vitrinedev] 
---

## Funcionalidades

*   Cadastro e autenticação de usuários
*   Upload e gerenciamento de imagens/posts
*   Visualização de posts públicos ou privados
*   Interface amigável construída com Bootstrap
*   Restrição de acesso a conteúdos conforme perfil do usuário

## Tecnologias utilizadas

*   Python 3.14
*   Django
*   Bootstrap
*   SQLite (padrão do Django, fácil de trocar por outro banco)
*   Amazon S3

## Como rodar o projeto

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/Thiago4596/Django-Alura-Space.git](https://github.com/Thiago4596/Django-Alura-Space.git)
    ```
2.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Prepare o banco de dados**
    ```bash
    python manage.py migrate
    ```
4.  **Crie um usuário administrador**
    ```bash
    python manage.py createsuperuser
    ```
5.  **Inicie o servidor de desenvolvimento**
    ```bash
    python manage.py runserver
    ```
6.  Acesse `http://localhost:8000` no navegador para usar a aplicação.

## Estrutura do projeto

Django-Alura-Space/ ├── manage.py ├── README.md ├── requirements.txt ├── <app_principal>/ │ ├── migrations/ │ ├── models.py │ ├── views.py │ └── ... └── ...

## Contribuição

Fique à vontade para abrir issues e pull requests com melhorias, correções ou novas funcionalidades!

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para informações mais detalhadas.
