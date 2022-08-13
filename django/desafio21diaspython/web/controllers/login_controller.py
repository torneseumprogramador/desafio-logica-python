from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from web.models import Contato
from ..seguranca.funcoes import set_cookie
import json

def index(request):
    return render(request, 'login/index.html', {"login": "true"})

def sair(request):
    response = HttpResponseRedirect("/login")
    set_cookie(response, 'usuario_logado', "", -1)
    return response

@require_http_methods(["POST"])
def logar(request):
    email = request.POST["email"]
    senha = request.POST["senha"]

    if email is None or email == "":
        return render(request, 'login/index.html', {"login": "true", "mensagem": "Email é obrigatório"})

    if senha is None or senha == "":
        return render(request, 'login/index.html', {"login": "true", "mensagem": "Senha é obrigatória"})

    contato = Contato.objects.get(email=email, senha=senha)

    if contato is None:
        return render(request, 'login/index.html', {"login": "true", "mensagem": "Email ou senha inválidos"})

    response = HttpResponseRedirect("/")
    usuario = {"id": contato.id, "email": contato.email, "nome": contato.nome}
    usuario_json = json.dumps(usuario)
    set_cookie(response, 'usuario_logado', usuario_json, 1)

    return response


