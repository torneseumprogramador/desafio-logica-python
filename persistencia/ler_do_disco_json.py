import json

f = open("clientes.json", "r")
try:
  clientes_json = f.read()
  clientes = json.loads(clientes_json)

  for cliente in clientes:
    print(f"{'=' * 30}")
    print(f"id: {cliente['id']}")
    print(f"Nome: {cliente['nome']}")
    print(f"Email: {cliente['email']}")

except Exception as e:
  print(e)
  print("Algo deu errado na leitura do arquivo")
finally:
  f.close()
