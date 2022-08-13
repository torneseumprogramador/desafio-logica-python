import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from web.models import Contato
from ..seguranca.funcoes import required_decorator, set_cookie, usuario_logado
# from django.views.decorators.csrf import csrf_exempt

@required_decorator
def index(request):
    # TODO usar um flash message
    mensagem = request.COOKIES.get('mensagem')
    contatos = Contato.objects.all()
    view_model = {"sucesso": mensagem, "sessao": usuario_logado(request)["nome"], "contatos": contatos }

    id = request.GET.get("id")
    if id is not None:
        view_model["contato"] = Contato.objects.get(id=id)

    custon_render = render(request, 'contato/index.html', view_model)
    response = HttpResponse(custon_render)
    set_cookie(response, "mensagem", "", -1)
    return response

# def excluir(request, id): # TODO correção no decorator
@required_decorator
def excluir(request):
    id = request.GET["id"]
    Contato.objects.filter(id=id).delete()
    return HttpResponseRedirect("/contato")

@required_decorator
def cadastrar(request):
    nome = request.POST["nome"]
    if nome == "" or nome is None:
        return render(request, 'contato/index.html', {
            "erro": "O nome é obrigatório"
        })

    email = request.POST["email"]
    if email == "" or email is None:
        return render(request, 'contato/index.html', {
            "erro": "O email é obrigatório"
        })

    senha = request.POST["senha"]
    if senha == "" or senha is None:
        return render(request, 'contato/index.html', {
            "erro": "O senha é obrigatória"
        })

    contato = Contato()
    contato.nome = nome
    contato.email = email
    contato.senha = senha
    contato.save()

    response = HttpResponseRedirect("/contato")

    # TODO Cadastrar em um flash message
    set_cookie(response, "mensagem", "Lead cadastrado com sucesso", 1)

    return response

@required_decorator
def alterar(request):
    id = request.GET["id"]
    nome = request.POST["nome"]
    if nome == "" or nome is None:
        return render(request, 'contato/index.html', {
            "erro": "O nome é obrigatório"
        })

    email = request.POST["email"]
    if email == "" or email is None:
        return render(request, 'contato/index.html', {
            "erro": "O email é obrigatório"
        })

    senha = request.POST["senha"]
    if senha == "" or senha is None:
        return render(request, 'contato/index.html', {
            "erro": "O senha é obrigatória"
        })

    contato = Contato.objects.get(id=id)
    contato.nome = nome
    contato.email = email
    contato.senha = senha
    contato.save()

    response = HttpResponseRedirect("/contato")

    # TODO Cadastrar em um flash message
    set_cookie(response, "mensagem", "Lead alterada com sucesso", 1)

    return response


# @csrf_exempt # decorator para desabilitar o csrf security
@required_decorator
def cadastrar_antigo_gravando_json(request):
    email = request.POST["email"]
    if email == "" or email is None:
        return render(request, 'contato/index.html', {
            "mensagem": "O email é obrigatório"
        })

    file = "db/leads.json"
    leads = []

    f = open(file, "r")
    try:
        leads_json = f.read()
        leads = json.loads(leads_json)
    except Exception as e:
        print(e)
        print("Algo deu errado na leitura do arquivo")
    finally:
        f.close()
    
    leads.append({"email": email})

    f = open(file, "w")
    try:
        leads_json = json.dumps(leads)
        f.write(leads_json)
    except Exception as e:
        print(e)
        print("Algo deu errado na escrita do arquivo")
    finally:
        f.close()

    return render(request, 'contato/index.html', {
        "mensagem": "Lead cadastrado com sucesso"
    })
