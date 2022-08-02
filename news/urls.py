from django.urls import path
from .views import IndexTemplateView, ListarListView, DetalheDetailView, CadastrarCreateView, AtualizarUpdateView, DeletarDeleteView

urlpatterns = [
    # path('', index, name='index_autores'),
    path('', IndexTemplateView.as_view(), name='index_autores'),
    path('autores', ListarListView.as_view(), name='listar_autores'),
    path('autores/cadastro', CadastrarCreateView.as_view(), name='cadastrar_autores'),
    path('autores/<int:pk>', DetalheDetailView.as_view(), name='detalhar_autores'),
    path('autores/atualizar/<int:pk>', AtualizarUpdateView.as_view(), name='atualizar_autores'),
    path('autores/deletar/<int:pk>', DeletarDeleteView.as_view(), name='deletar_autores'),
]
