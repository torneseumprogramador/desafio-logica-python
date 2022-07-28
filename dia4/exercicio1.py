"""
Faça um programa para calcular números
solicite que o seu usuario digite 4 números
faça a soma do primeiro numero, com o ultimo numero
depois faça a multiplicação, com os números do meio
ao final some o resultado da soma, com o resultado da multiplicação

se o resultado total for > do que 100 mostrar

=========================
O resultado alcançado foi xxx parabéns
=========================

se o resultado total for <= do que 100 mostrar

=========================
O resultado alcançado foi xxx e ficou abaixo da expectativa
=========================
"""

print("Programa para calcular número")

print("Digte o número 1")
numero_um = int(input())

print("Digte o número 2")
numero_dois = int(input())
print("Digte o número 3")
numero_tres = int(input())
print("Digte o número 4")
numero_quatro = int(input())

somar_primeiro_ultimo = numero_um + numero_quatro
multiplicacao_numero_meio = numero_dois * numero_tres

somar_resultados = somar_primeiro_ultimo + multiplicacao_numero_meio

if somar_resultados > 100:
    print("=========================")
    print(f"O resultado alcançado foi {somar_resultados} parabéns")
    print("=========================")
else:
    print("=========================")
    print("O resultado alcançado foi xxx e ficou abaixo da expectativa")
    print("=========================")
