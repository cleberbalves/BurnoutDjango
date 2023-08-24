from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('teste/', views.exibir_pagina_teste, name='teste'),  # Usando 'exibir_pagina_teste' aqui
    path('depoimentos/', views.depoimentos_view, name='depoimentos'),
    path('contatos/', views.contatos_view, name='contatos'),
    path('excluir_depoimento/<str:texto>/', views.excluir_depoimento, name='excluir_depoimento'),
    path('resultado/', views.exibir_pagina_resultado, name='resultado'),  # Usando 'exibir_pagina_resul
    path('cadastro/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('listagem/', views.listar_pessoas, name='listar_pessoas'),
    path('editar/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('excluir/<int:id>/', views.excluir_pessoa, name='excluir_pessoa')
]
