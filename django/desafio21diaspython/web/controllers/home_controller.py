from django.shortcuts import render


def index(request):
    resposta = {}
    resposta["conteudo"] = "Estou passando uma chave chamado conteudo para meu template"
    return render(request, 'home/index.html', resposta)

def sobre(request):
    return render(request, 'home/sobre.html')
