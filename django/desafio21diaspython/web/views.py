from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    resposta = {}
    resposta["conteudo"] = "Estou passando uma chave chamado conteudo para meu template"
    return render(request, 'home/index.html', resposta)

def sobre(request):
    return render(request, 'home/sobre.html')

def contato(request):
    return render(request, 'home/contato.html')

def html_bruto(request):
    return HttpResponse("<h1>respondendo por html</h1>")

def json(request):
    resposta = {}
    resposta["conteudo"] = "Agora com API JSON"
    return JsonResponse(resposta)

def xml_bruto(request):
    xml_bruto = '<?xml version="1.0" encoding="UTF-8"?><bookstore><book category="cooking"><title lang="en">Everyday Italian</title><author>Giada De Laurentiis</author><year>2005</year><price>30.00</price></book></bookstore>'
    return HttpResponse(xml_bruto, content_type="text/xml")
