from django.shortcuts import render
from ..seguranca.funcoes import required_decorator, usuario_logado


@required_decorator
def index(request):
    resposta = {}
    resposta["conteudo"] = "Estou passando uma chave chamado conteudo para meu template"
    resposta["sessao"] = usuario_logado(request)["nome"]
    
    return render(request, 'home/index.html', resposta)

def sobre(request):
    return render(request, 'home/sobre.html')
