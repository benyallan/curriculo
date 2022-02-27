from django.shortcuts import render
from core.models import DadosPessoais


def welcome(request):
    pessoa = DadosPessoais.objects.first()
    dados = {'pessoa': pessoa}
    return render(request, 'index.html', dados)
