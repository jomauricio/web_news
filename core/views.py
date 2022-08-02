from multiprocessing import context
from django.shortcuts import render
from news.models import Autor, Noticia
# Create your views here.


def index(request):
    autores = Autor.objects.all()[0:5]
    noticias = Noticia.objects.all()[0:5]
    contexto = {'autores': autores, 'noticias': noticias}
    return render(request, 'base.html', contexto)