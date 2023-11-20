# from . import views
from blog import views
from django.urls import path

# DEFININDO UM NAMESPACE PARA ESTE APP
app_name = 'blog'

# blog/ ----> endpoint RAIZ, colocado antes das URLS abaixo
# Fazemos isso para aninhar endpoints, com base em um endpoint raiz.
urlpatterns = [
    path('', views.blog, name='home'),
    # Nesse endpoint, passamos somente o parametro da URL,
    # Então, se deixarmos a primeira parte do endpoint em branco
    # Vai chamar a URL raiz /blog/
    # E então, neste outro path abaixo, passamos só um parametro
    # O que acontece aqui na prática é: /blog/<int:id>
    path('<int:post_id>', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
