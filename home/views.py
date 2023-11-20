from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# No arquivo de URLs, tenho que chamar os métodos. Após passar o caminho deles.


def home(request):
    print('HOME')

    context = {
        "text": "Olá home"
    }

    # RENDER ---> busca arquivos dos diretórios: TEMPLATES e BASE
    return render(
        request,
        'home/index.html',  # Busca automaticamente todos os arquivos que estão dentro da pasta TEMPLATES na raiz da pasta do APP
        context=context
    )
