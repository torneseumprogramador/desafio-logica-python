"""
Utilizando Dict, faça:

Danilo é dono de uma escola de programação, faça um programa
solicite a quantidade de alunos, capture 3 notas de alunos
no final do programa mostre um relatório identificando se os alunos
estão aprovados, reprovados ou em recuperação

Calculo da média
media = (n1+n2+n3)/3

Regra de aprovação:
Notas abaixo de 5 = Reprovado
Notas de 5 até 7 = Recuperção
Notas acima de 7 = Aprovado

Exemplo de lista:

=============[Lista de alunos]==============
Nome: Danilo
Média: 7.5
Situação: Aprovado
-----------------------
Nome: Lana
Média: 5.5
Situação: Recuperacao
-----------------------
"""
import os

lista_de_aluno = []
quantidade_de_notas = 3

os.system("clear")

print("============[ CADASTRO DE NOTA ]================\n")
quantidade_aluno = int(input("Informe a quantidade de alunos:"))
for i in range(0, quantidade_aluno):
    media = 0
    notas = []
    situacao = "Aprovado"
    aluno = {}

    aluno["nome"] = input(f"\nInforme nome do aluno {i+1}:")

    for y in range(0, quantidade_de_notas):
        nota = 0
        notas.append(float(input(f"Digite nota {y + 1}: ")))

    media = float("{:0.2f}".format(sum(notas) / quantidade_de_notas))
    aluno["media"] = media
    aluno["notas"] = notas

    if media >= 5 and media <= 7:
        situacao = "Recuperação"
    elif media < 5:
        situacao = "Reprovado"

    aluno["situacao"] = situacao
    lista_de_aluno.append(aluno)
    del aluno

print("\n============[ Lista de alunos ]================\n")
for aluno in lista_de_aluno:
    for chave, valor in aluno.items():
        print(f"{chave}: {valor}")
    print("\n")
print("===============================================\n")
