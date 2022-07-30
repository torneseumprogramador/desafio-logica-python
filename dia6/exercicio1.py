"""
Claudio é um matemático que precisa de um programa para facilitar
o calulo de uma tabuada, faça um programa que solicite 1 número
e crie a tabuada do mesmo, exemplo:

Digite um numero para calcular a tabuada?
5

1 x 5 = 5
2 x 5 = 10
...
10 x 5 = 50
"""

print("==========[Programa de calculo tabuada]==========")
numero = int(input("Digite um numero\n"))

# forma manual
print("=======[manual]======")
print(f"1 x {numero} = {numero*1}")
print(f"2 x {numero} = {numero*2}")
print(f"3 x {numero} = {numero*3}")
print(f"4 x {numero} = {numero*4}")
print(f"5 x {numero} = {numero*5}")
print(f"6 x {numero} = {numero*6}")
print(f"7 x {numero} = {numero*7}")
print(f"8 x {numero} = {numero*8}")
print(f"9 x {numero} = {numero*9}")
print(f"10 x {numero} = {numero*10}")

# utilizando loop
print("=======[while]======")
i = 1
while i <= 10:
    print(f"{i} x {numero} = {numero*i}")
    i += 1

# utilizando for
print("=======[for]======")
for i in range(1, 11):
    print(f"{i} x {numero} = {numero*i}")
