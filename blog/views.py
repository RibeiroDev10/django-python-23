from django.http import HttpResponse
from django.shortcuts import render
from blog.data import posts # Todos os posts (arquivo JSON/DICT)
from typing import Any
from django.http import HttpRequest, Http404

# Create your views here.
# No arquivo de URLs, tenho que chamar os métodos. Após passar o caminho deles.


def blog(request):
    print('BLOG')

    context = {
        "text": "Olá blog!",
        "posts": posts
    }

    return render(
        request,
        'blog/index.html',  # templates/blog/home.html ---> para distinguir arquivos/diretorios de templates de cada APP
        context=context  # As chaves dessa variável, se tornam variáveis, no index.html passado acima.
    )

# view ---------- POST
def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            # Recebe o POST inteiro que contém aquela chave ID
            # Que foi passada no parametro do request
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        'post': found_post,
        'title': found_post['title'] + ' - '
    }

    return render(
        request,
        'blog/post.html',
        context
    )
# view ---------- POST


def exemplo(request):
    print('exemplo')

    context = {
        "text": "Olá exemplo!",
        "title": "Essa é uma página de exemplo!",
    }

    return render(  # Pega arquivos HTML dentro do diretório TEMPLATES na pasta RAIZ.
        request,
        'blog/exemplo.html',  # templates/blog/exemplo.htlm ---> para distinguir arquivos/diretorios de templates de cada APP
        context=context
    )
