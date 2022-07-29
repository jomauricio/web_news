from django.urls import path
from .views import deletar, index, detalhar, listar, cadastrar, atualizar, deletar

urlpatterns = [
    path('', index),
    path('autores', listar),
    path('autores/cadastro', cadastrar),
    path('autores/<int:id>', detalhar),
    path('autores/atualizar/<int:id>', atualizar),
    path('autores/deletar/<int:id>', deletar),
]
