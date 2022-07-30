"""
Faca um programa para ter um menu onde
o usuario digitando:
1 = Execute a tabuada
2 = execute a tabuada com iterador
3 = saia do programa
"""
import os
import time

while True:
    print("\nEscolhe uma opção:\n")
    print("1 = Execute a tabuada")
    print("2 = execute a tabuada com iterador")
    print("3 = saia do programa")
    valor = int(input())
    os.system("clear")

    if valor == 1:
      numero = int(input("Digite um número para calcular a tabuada?\n"))
      i = 1
      while i <= 10:
        print(f" {numero} x {i} = {numero * i}") 
        i += 1
    elif valor == 2:
      numero = int(input("Digite um número para calcular a tabuada?\n"))
      iterador = int(input(f"Quantas vezes deseja multiplicar o número {numero}?\n"))
      i = 1
      while i <= iterador:
        print(f" {numero} x {i} = {numero * i}") 
        i += 1
    elif valor == 3:
        break

    time.sleep(5)
    os.system("clear")
