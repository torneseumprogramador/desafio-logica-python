"""
O professor Danilo, necessita organizar os exercicios passados no desafio
de python, com isso deseja que seus alunos faça um programa utilizando
funções para organizar todos os exercícios passados em um menu.
Ou seja, crie um program que organize os exercicos em funções
dos dias 2,3,4,5,6,7,8
e acesse o exercicio através de uma organização em menu
"""
import dia2
import dia3
import dia4
import utils

while True:
  utils.limpar_tela()
  print("=== Bem vindo ao programa ===\n")
  print("Digite um opção:\n")
  print("1 - Chama o exercicio do dia 2")
  print("2 - Chama o exercicio do dia 3")
  print("3 - Chama o exercicio do dia 4")
  print("10 - Sair do programa")

  opcao = int(input())

  if opcao == 10:
    break
  elif opcao == 1:
    dia2.exercicio()
  elif opcao == 2:
    dia3.exercicio()
  elif opcao == 3:
    dia4.exercicio()
  else:
   print("Em construção")

  utils.espera_em_segundos(3)
