from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_carro>', views.ver_carro, name='detalhes'), # esse '<int:id_carro>' mostra o parametro que a funcao recebeu
    path('busca/', views.busca, name='busca'),
]