from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import datetime

def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60 
    else:
        max_age = days_expire * 24 * 60 * 60
    
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires
    )

def required_decorator(func):
    def containing_func(*args):
        request = args[0]

        value = request.COOKIES.get('cookie_name')

        # if value is None:
        #     return HttpResponseRedirect("http://www.torneseumprogramador.com.br/")

        try:
            print("=========[DECORATOR]============")
            print("=========[cookie]============")
            print(value)
            print("=========[args]============")
            print(args)
            print("=============================")
        except Exception as e:
            raise e
        return func(*args)
    return containing_func


@require_http_methods(["GET", "POST"])
@csrf_exempt
@required_decorator
def index(request):
    # status não permitido
    # return HttpResponse("Não permitido", {}, 403)

    # resposta = {}
    # resposta["conteudo"] = "Agora com API JSON"
    # return JsonResponse(resposta, status=201)

    if request.method == 'POST':
        print("======= POST ==========")

    resposta = {}
    value = request.COOKIES.get('cookie_name')
    resposta["conteudo"] = f"Estou passando uma chave chamado conteudo para meu template - {value}"

    response = HttpResponse(render(request, 'home/index.html', resposta))
    set_cookie(response, 'cookie_name', '--danilo--')

    return response

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
