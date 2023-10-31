from django.contrib import admin

# Register your models here.
from .models import Atleta, UltimaPartida

class AtletaAdmin(admin.ModelAdmin):
	list_display=('nome', 'gols', 'assistencias')
	
admin.site.register(Atleta, AtletaAdmin)
admin.site.register(UltimaPartida)
