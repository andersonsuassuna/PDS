from django.shortcuts import render

from . import models

# Create your views here.
def listagem(request):
    produtos = models.Produto.objects.all()
    return render(request, 'produtos/listagem.html', {'produtos': produtos})

def detalhes(request, id):
    produto = models.Produto.objects.get(id=id)
    return render(request, 'produtos/detalhes.html', {'produto':produto})