import os
"""
=========== Sistema de combustível ============
Digite a quantidade de litros padrão:
Digite a quantidade de litros para preencher a quantidade total:
Digite a valor do litro:
A quantidade que litros que ficou no posto foi: xxx
Estamos com a capacidade de xxx% de litros em nossos tanques
O valor total investido em litros no posto de gasolina é R$xxx
:::: Chegou um cliente, bora vender ? ::::
Digite o nome do cliente:
Digite o R$ "valor" que o senhor(a) xxx que deseja colocar:
:::: Ficou com xxxx litros de um total de yyy de combustível no tanque do posto :::::
:::: O posto está operando agora com x% de sua capacidade de combustivel :::::
"""

print("========== Sistema de combustível ===============")
print("Digite a quantidade de litros padrão:")
litro_posto = float(input())
print("Digite a quantidade de litros para preencher a quantidade total:")
atual_posto = float(input())
print("Digite a valor do litro:")
valor_litro = float(input())
# TODO Capturar o valor por litro

os.system('clear')
print("========== Sistema de combustível ===============")
print(f"\nA capacidade de nossos tanques é: {litro_posto} litros")
print(f"A quantidade que ficou no posto foi: {atual_posto} litros")
total_porcentagem = atual_posto / litro_posto * 100
print("Estamos com a capacidade de {:0.2f}% em nossos tanques".format(
    total_porcentagem))
valor_invertido = atual_posto * valor_litro
print(
    f"O valor total investido em litros no posto de gasolina é R${valor_invertido}")

print(f"\n:::: Chegou um cliente, bora vender? :::::")
print(f"Digite o nome do cliente:")
nome_consumidor = input()
print(
    f"Digite o R$ \"valor\" que o senhor(a) {nome_consumidor} que deseja colocar:")
valor_do_cliente = float(input())

# TODO calcular o valor em litros
quantidade_cliente = valor_do_cliente / valor_litro

sobrou_no_tanque_do_posto = atual_posto - quantidade_cliente
total_porcentagem = sobrou_no_tanque_do_posto / litro_posto * 100

print("\n::: Ficou com {:0.2f} litros de um total de {} litros de combustível no tanque do posto ::::".format(
    sobrou_no_tanque_do_posto, atual_posto))
print("::: O posto está operando agora com {:0.2f}% de sua capacidade de combustível :::".format(
    total_porcentagem))