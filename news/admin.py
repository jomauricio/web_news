from django.contrib import admin

from .models import Autor, Noticia

class AutorAdmin(admin.ModelAdmin):
    model = Autor
    list_display = ('nome',)
    search_fields = ['nome']

class NoticiaAdmin(admin.ModelAdmin):
    model = Noticia
    search_fields = ['titulo']
    list_display = ('titulo', 'autor_id', 'tags', 'data_pub')
    list_filter = ('autor_id', 'tags')

admin.site.register(Autor, AutorAdmin)
admin.site.register(Noticia, NoticiaAdmin)