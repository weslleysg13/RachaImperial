from django.urls import path
from .views import index, estatisticas

urlpatterns = [
    path('', index, name='index'),
    path('estatisticas', estatisticas, name='estatisticas'),
]
