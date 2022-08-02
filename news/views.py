from urllib import request

from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AutorForm, NoticiaForm
from .models import Autor, Noticia

# Create your views here.

class IndexTemplateView(TemplateView):
    template_name='autor/index.html'

# def index(request):
#     return render(request, 'autor/index.html')

class ListarListView(ListView):
    model=Autor
    template_name='autor/listar.html'
    context_object_name='autores'

# def listar(request):
#     autores = Autor.objects.all()
#     return render(request, 'autor/listar.html', {'autores':autores})

class DetalheDetailView(DetailView):
    model=Autor
    template_name='autor/detalhar.html'
    context_object_name='aut'

# def detalhar(request, id):
#     autor = Autor.objects.get(id=id)
#     return render(request, 'autor/detalhar.html', {'aut': autor})

class CadastrarCreateView(CreateView):
    model=Autor
    template_name='autor/cadastrar.html'
    form_class=AutorForm
    success_url='/news/autores'

# def cadastrar(request):
#     if request.method == 'POST':
#         form = AutorForm(request.POST)
#         if form.is_valid():
#             autor = form.save()
#             return redirect('/news/autores')
#     else:
#         form = AutorForm()
    
#     return render(request, 'autor/cadastrar.html', {'form':form})

class AtualizarUpdateView(UpdateView):
    model=Autor
    template_name='autor/atualizar.html'
    form_class=AutorForm
    success_url='/news/autores'

# def atualizar(request, id):
#     autor = Autor.objects.get(id=id)
#     form = AutorForm(instance=autor)
#     if request.method == 'POST':
#         form = AutorForm(request.POST, instance=autor)
#         if form.is_valid():
#             autor = form.save()
#             return redirect('/news/autores')
#         else:
#             return render(request, 'autor/atualizar.html', {'form':form, 'autor':autor})
#     else:
#         return render(request, 'autor/atualizar.html', {'form':form, 'autor':autor})

class DeletarDeleteView(DeleteView):
    model=Autor
    template_name_suffix=''
    template_name='autor/autor_delete.html'
    success_url='/news/autores'

# def deletar(request, id):
#     autor = Autor.objects.get(id=id)
#     autor.delete()
#     return redirect('/news/autores')
