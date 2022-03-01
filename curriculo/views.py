from django.shortcuts import render
from core.models import DadosPessoais, Telefone


def welcome(request):
    pessoa = DadosPessoais.objects.first()
    telefones = Telefone.objects.filter(person=pessoa)
    dados = {'pessoa': pessoa, 'telefones': telefones}
    return render(request, 'index.html', dados)
