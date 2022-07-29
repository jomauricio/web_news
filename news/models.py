from django.db import models

# Create your models here.

class Autor(models.Model):

    nome = models.CharField('Nome', max_length=250)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome

class Noticia(models.Model):

    CHOICES_TAGS = [
        ('Urgente','Urgente'),
        ('Saúde','Saúde',),
        ('Politica','Politica',)
    ]

    titulo = models.CharField('Titulo', max_length=250)
    conteudo = models.TextField('Conteudo')
    tags = models.CharField('Tags', choices=CHOICES_TAGS, max_length=20)
    data_pub = models.DateTimeField('Data de publicação')
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Autor')

    def __str__(self):
        return self.titulo

