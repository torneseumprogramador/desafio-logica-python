import json

from django.shortcuts import render


def index(request):
    return render(request, 'contato/index.html')

def cadastrar(request):
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
