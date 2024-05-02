from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa


def ver_produto(request):
    #return HttpResponse('estou no ver')
    if request.method == "GET":
        nome = 'Leandro LL'
        return render(request, 'ver_produto.html', {'nome': nome})
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        pessoa = Pessoa(nome=nome, idade=idade)
        pessoa.save()

        pessoas_cad = Pessoa.objects.all();

        #pessoas_cad = Pessoa.objects.filter(nome=nome);

        return HttpResponse([*pessoas_cad])

def inserir_produto(request):
    #return HttpResponse('estou no inserir')
    return render(request, 'inserir_produto.html')