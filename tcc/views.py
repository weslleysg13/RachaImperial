from django.shortcuts import render

# Create your views here.

from .models import Atleta

def index(request):
	# Cálculo dos 7 primeiros artilheiros
	artilheiros = Atleta.objects.all().order_by('-gols').values()
	# Cálculo dos 7 primeiros líderes em Assistências
	assistentes = Atleta.objects.all().order_by('-assistencias').values()
	# Cálculo 
	context = {
		'artilheiros': artilheiros,
		'assistentes': assistentes
	}
	return render(request, 'index.html', context)

def serie(request):
	return render(request, 'serie.html')

def jogo(request):
	return render(request, 'jogo.html')

def estatisticas(request):
	# Cálculo dos Artilheiros
	artilheiros = Atleta.objects.all().order_by('-gols').values()
	# Cálculo das Assistências
	assistentes = Atleta.objects.all().order_by('-assistencias').values()
	# Cálculo dos Amarelos
	amarelados = Atleta.objects.all().order_by('-amarelos').values()
	# Cálculo dos Vermelhos
	expulsos = Atleta.objects.all().order_by('-vermelhos').values()
	# Cálculo das Vitórias
	vitorias = Atleta.objects.all().order_by('-vitorias').values()
	# Cálculo dos Deivids
	deivids = Atleta.objects.all().order_by('-deivid').values()
	# Cálculo dos Puskas
	puskas = Atleta.objects.all().order_by('-puskas').values()
	# Cálculo dos Bolas Cheias
	cheias = Atleta.objects.all().order_by('-bolaCheia').values()
	# Cálculo dos Bolas Murchas
	murchas = Atleta.objects.all().order_by('-bolaMurcha').values()
	context = {
		'artilheiros': artilheiros,
		'assistentes': assistentes,
		'amarelados' : amarelados,
		'expulsos' : expulsos,
		'vitorias' : vitorias,
		'deivids' : deivids,
		'puskas' : puskas,
		'cheias' : cheias,
		'murchas': murchas,
	}
	return render(request, 'estatisticas.html', context)
