# Django Alura Space
Este é o projeto "Django Alura Space", um aplicativo web desenvolvido com Django durante os cursos da Alura. O objetivo é gerenciar e compartilhar conteúdos, como imagens e posts, para usuários de uma comunidade ou espaço, aplicando os principais conceitos e práticas do framework Django.

---

## Vitrine.Dev - Informações para a Alura

✨ Thiago, Django Alura Space
🏷️ Tecnologias, Django, Python, Bootstrap, SQLite, Amazon S3
[https://i.imgur.com/sua-imagem-de-capa.png#vitrinedev] 

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
