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

print("========== Sistema de combustível ===============")
print("Digite a quantidade de litros padrão:")
litro_posto = float(input())
print("Digite a quantidade de litros para preencher a quantidade total:")
atual_posto = float(input())

print(f"A capacidade de nossos tanques é: {litro_posto} litros")
print(f"A quantidade que ficou no posto foi: {atual_posto} litros")
total_porcentagem = atual_posto / litro_posto * 100
print("Estamos com a capacidade de {:0.2f}% em nossos tanques".format(total_porcentagem))

print(f":::: Chegou um cliente, bora vender? :::::")
print(f"Digite o nome do cliente:")
nome_consumidor = input()

print(f"Qual a quantidade de litros que o senhor(a) {nome_consumidor} que deseja colocar ?")
quantidade_cliente = float(input())

sobrou_no_tanque_do_posto = atual_posto - quantidade_cliente
total_porcentagem = sobrou_no_tanque_do_posto / litro_posto * 100

print(f"::: Ficou com {sobrou_no_tanque_do_posto} litros de um total de {atual_posto} litros de combustível no tanque do posto ::::")
print("::: O posto está operando agora com {:0.2f}% de sua capacidade de combustível :::".format(total_porcentagem))
