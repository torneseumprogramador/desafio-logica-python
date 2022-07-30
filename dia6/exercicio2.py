"""
Claudio é um matemático que precisa de um programa para facilitar
o calulo de uma tabuada, faça um programa que solicite 1 número multiplicador
e 1 número do iterador. Crie a tabuada do mesmo, exemplo:

Digite um numero para calcular a tabuada?
5
Digite um numero para o iterador da tabuada
3

1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
"""

print("==========[Programa de calculo tabuada]==========")
numero = int(input("Digite um numero da tabuada\n"))
iterador = int(input("Digite um numero iterador\n"))

# forma manual
# print("=======[manual]======")
# if iterador == 1:
#     print(f"1 x {numero} = {numero*1}")
# elif iterador == 2:
#     print(f"1 x {numero} = {numero*1}")
#     print(f"2 x {numero} = {numero*2}")
# elif iterador == 3:
#     print(f"1 x {numero} = {numero*1}")
#     print(f"2 x {numero} = {numero*2}")
#     print(f"3 x {numero} = {numero*3}")
# # Forma erradaaaaa

# utilizando loop
print("=======[while]======")
i = 1
while i <= iterador:
    print(f"{i} x {numero} = {numero*i}")
    i += 1

# utilizando for
print("=======[for]======")
for i in range(1, iterador+1):
    print(f"{i} x {numero} = {numero*i}")
