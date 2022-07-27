"""
Leandro tem um posto de combustível e precisa encher o tanque do posto
Faça um programa que digite a quantidade de litros do tanque de combustivel atual
suporta.
e receba um valor para preencher o tanque de combustível deixando o mesmo cheio
colocando o valor atual do tanque

Mostrar a porcentagem da capacidade do tanque

e quando chegar um cliente, colocar o combustível 
depois mostrar a quantidade de litros que ficou no tanque do posto


=========== Sistema de combustível ============
Digite a quantidade de litros padrão:

Digite a quantidade de litros para preencher a quantidade total:

A quantidade que litros que ficou no posto foi: xxx
Estamos com a capacidade de xxx% de litros em nossos tanques

:::: Chegou um cliente, bora vender ? ::::
Digite o nome do cliente:
Digite o valor que o senhor(a) xxx que deseja colocar:

:::: Ficou com xxxx litros de um total de yyy de combustível no tanque do posto :::::
:::: O posto está operando agora com x% de sua capacidade de combustivel :::::
"""

print("------ SISTEMA DE COMBUSTÍVEL--------")
print("digite a quantidade de litro padrão")
litro_padrao = input()

print("digite a quantidade de litros para preencher a qtd total")
qtd_atual_posto = input()

print("A quantidade de litro que ficou no posto foi " + qtd_atual_posto)

print("------ Chegou um cliente, bora vender???------")
print("digite o nome do cliente")
Nome = input()

print("digite o valor que o senhor(a) " + Nome + " deseja colocar")
qtd_cliente = input()

sobra = float(qtd_atual_posto) - float(qtd_cliente)

print(f"Ficou com {sobra} litros de um total de {qtd_atual_posto} de combustivel no tanque do posto")