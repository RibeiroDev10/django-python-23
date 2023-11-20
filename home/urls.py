from django.urls import path

from . import views

# DEFININDO UM NAMESPACE PARA ESTE APP
app_name = 'home'
    
# home/ ----> endpoint RAIZ, colocado antes das URLS abaixo
# Fazemos isso para aninhar endpoints, com base em um endpoint raiz.
urlpatterns = [
    path('', views.home, name="home"),  # home/ ----> endpoint RAIZ
]
