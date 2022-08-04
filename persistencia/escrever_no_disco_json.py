import json

cliente = {
  "id": 1,
  "nome": "Wilian",
  "email": "wilian@teste.com",
}

clientes = []
clientes.append(cliente)

f = open("clientes.json", "w")
try:
  clientes_json = json.dumps(clientes)
  f.write(clientes_json)
except Exception as e:
  print(e)
  print("Algo deu errado na escrita do arquivo")
finally:
  f.close()
