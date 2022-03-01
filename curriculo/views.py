from django.shortcuts import render
from core.models import DadosPessoais, Telefone, RedesSociais


def welcome(request):
    pessoa = DadosPessoais.objects.first()
    telefones = Telefone.objects.filter(person=pessoa)
    redessociais = RedesSociais.objects.filter(person=pessoa)
    
    dados = {
                'pessoa': pessoa, 'telefones': telefones, 
                'redessociais': redessociais
            }
    return render(request, 'index.html', dados)
