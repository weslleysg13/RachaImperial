from django.db import models
from stdimage.models import StdImageField

# Create your models here.

class Atleta(models.Model):
        nome = models.CharField('Nome', max_length=100)
        gols = models.IntegerField('Gols', default=0)
        assistencias = models.IntegerField('Assistências', default=0)
        vitorias = models.IntegerField('Vitórias', default=0)
        amarelos = models.IntegerField('Amarelos', default=0)
        vermelhos = models.IntegerField('Vermelhos', default=0)
        deivid = models.IntegerField('Deivid', default=0)
        puskas = models.IntegerField('Puskas', default=0)
        bolaCheia = models.IntegerField('Bola Cheia', default=0)
        bolaMurcha = models.IntegerField('Bola Murcha', default=0)
        def __str__(self):
                return self.nome

class UltimaPartida(models.Model):
        imagem = StdImageField('Imagem', upload_to='tcc/static/images', delete_orphans=True)