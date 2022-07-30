from urllib import request

from django.shortcuts import redirect, render

from .forms import AutorForm, NoticiaForm
from .models import Autor, Noticia

# Create your views here.

def index(request):
    return render(request, 'autor/index.html')

def listar(request):
    autores = Autor.objects.all()
    return render(request, 'autor/listar.html', {'autores':autores})

def detalhar(request, id):
    autor = Autor.objects.get(id=id)
    return render(request, 'autor/detalhar.html', {'autor': autor, 'logomarca': 'O melhor site!!!'})

def cadastrar(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            return redirect('/news/autores')
    else:
        form = AutorForm()
    
    return render(request, 'autor/cadastrar.html', {'form':form})

def atualizar(request, id):
    autor = Autor.objects.get(id=id)
    form = AutorForm(instance=autor)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            autor = form.save()
            return redirect('/news/autores')
        else:
            return render(request, 'autor/atualizar.html', {'form':form, 'autor':autor})
    else:
        return render(request, 'autor/atualizar.html', {'form':form, 'autor':autor})

def deletar(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect('/news/autores')
