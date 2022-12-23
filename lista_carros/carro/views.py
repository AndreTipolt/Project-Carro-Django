from django.shortcuts import render, get_object_or_404, redirect
from .models import Carro
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.http import Http404

def index(request):
    # carros = Carro.objects.all()
    carros = Carro.objects.order_by('nome')

    paginator = Paginator(carros, 4) # Ele recebe o dicionario carros e faz uma paginação de 4 em 4 itens

    page = request.GET.get('p')

    carros = paginator.get_page(page)

    return render(request, 'carro/index.html', {
        'carros': carros 
    })





def ver_carro(request, id_carro):
    # carro = Carro.objects.get(id=id_carro)
    carro = get_object_or_404(Carro, id=id_carro)
    return render(request, 'carro/detalhes.html',{
        'carro': carro
    })


def busca(request):
    termo = request.GET.get('termo')

    if not termo:
        messages.add_message(request, messages.ERROR, 'Digite um nome de carro válido.')
        return redirect('index')

    carros = Carro.objects.order_by('nome').filter(
        Q(nome__icontains=termo) | Q(marca__icontains=termo)
    )

    return render(request, 'carro/busca.html', {
        'carros' : carros
    })