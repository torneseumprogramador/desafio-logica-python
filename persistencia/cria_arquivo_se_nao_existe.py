import json
from os.path import exists

file_exists = exists("clientes.json")

print(f"Existe? [{file_exists}]")

if not file_exists:
  f = open("clientes.json", "w")
  try:
    clientes_json = json.dumps([])
    f.write(clientes_json)
  except Exception as e:
    print(e)
    print("Algo deu errado na escrita do arquivo")
  finally:
    f.close()
