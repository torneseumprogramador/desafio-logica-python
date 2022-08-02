import os
import time


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
