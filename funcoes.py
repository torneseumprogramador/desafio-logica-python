import os
import time


def funcaoSemParametros(): # cria funcao
    print("Uma funcao")
funcaoSemParametros() # executa funcao


def funcaoComParametros(parametro): # cria funcao
    print(parametro + 1)
funcaoComParametros(1) # executa funcao


def funcaoComParametrosValorPadrao(parametro = 2): # cria funcao
    print(parametro + 1)
funcaoComParametrosValorPadrao() # executa funcao


def funcaoComMaisDeUmParametro(numero1, numero2): # cria funcao
    print(numero1, numero2, "", 1)
funcaoComMaisDeUmParametro(1,3) # executa funcao


def funcaoComRetorno(numero1): # cria funcao
    return numero1 + 1
print(funcaoComRetorno(10)) # executa funcao


def funcaoComArrayDeParametros(*args): # cria funcao
    print(f"Indice 0 - {args[0]}")
    print(args)
funcaoComArrayDeParametros(1,2,3,4,6) # executa funcao


time.sleep(2)
os.system("clear")

def mostrar(numero):
    return f":: Mostrando uma informação na tela {numero}::"

while True :
    print("=== Bem vindo ao programa ===")
    print("Digite uma opção:")
    print("1 - Mostrar algo na tela")
    print("2 - Mostrar algo na tela mais 1")
    print("3 - Mostrar algo na tela mais 2")
    print("4 - Mostrar algo na tela mais 3")
    print("5 - Mostrar algo na tela mais 4")
    print("10 - Sair do programa")

    opcao = int(input())
    os.system("clear")

    if opcao == 10:
        break
    elif opcao == 1:
        print(mostrar(""))
    elif opcao == 2:
        print(f"{ mostrar(1) }")
    elif opcao == 3:
        print(f"{ mostrar(2) }")
    elif opcao == 4:
        print(f"{ mostrar(3) }")
    elif opcao == 5:
        print(f"{ mostrar(4) }")
    else:
        print("Opção inválida")

    time.sleep(2)
    os.system("clear")
