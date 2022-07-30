# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_for_loops.asp


# exemplo com continue
print("Exemplo while true/continue") # while = enquanto
while True:
    numero = int(input("Digite 0 para sair\n"))
    
    if numero == 10:
        continue

    print(f"Você digitou o número {numero}")

    if numero == 0:
        break


# eu não sei exatamente quando tenho que terminar
print("Exemplo while") # while = enquanto
while True:
    numero = int(input("Digite 0 para sair\n"))
    print(f"Você digitou o número {numero}")
    if numero == 0:
        break

# exemplo de while que poderia ser utilizado com for
i = 1
while i < 6:
  print(i)
  i += 1

# eu sei exatamente quando começa e termina
print("Exemplo for")  # for = para
inicial = int(input("Digite o numero incial\n"))
final = int(input("Digite o numero final\n"))
for x in range(inicial, final+1):
    print(x)
