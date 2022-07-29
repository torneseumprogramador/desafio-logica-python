"""
Danilo, um professor de tecnoliga, empresario no torne-se um programador,
deseja um sóftware que ajude a calcular a média de nota de um aluno,
faça um programa onde solicite o nome do aluno, tres notas do mesmo
depois faça o calculo para saber se o mesmo está aprovado:

exemplo média aritimérica:
(a+b+c)/3

regras para aprovação
 
se o aluno tirou a média aritimética < 5, aluno está reprovado
se o aluno tirou a média aritimética entre 5 e 7, aluno está em recuperação
se o aluno tirou a média aritimética > 7, aluno está aprovado

utilize a sua criatividade e agrade o seu professor, com a melhor experiencia

"""

nome = print("=========== [Calculo de média de alunos] ==========")

nome = input("Digite o nome do aluno\n")
nota1 = float(input(f"Digite a nota de número 1 - {nome}\n"))
nota2 = float(input(f"Digite a nota de número 2 - {nome}\n"))
nota3 = float(input(f"Digite a nota de número 3 - {nome}\n"))

media = (nota1+nota2+nota3)/3

if media < 5:
    resultado = "reprovado"
elif media >= 5 and media <= 7:
    resultado = "recuperação"
else:
    resultado = "Aprovado"

print("=========== [Resutado] ==========")
media_formatada = "{:0.2f}".format(media)
print(f"Situação do aluno {nome} é de {resultado} pois sua média foi {media_formatada}")
