"""
O professor Danilo, necessita organizar os exercicios passados no desafio
de python, com isso deseja que seus alunos faça um programa utilizando
funções para organizar todos os exercícios passados em um menu.
Ou seja, crie um program que organize os exercicos em funções
dos dias 2,3,4,5,6,7,8
e acesse o exercicio através de uma organização em menu
"""

import os


def limpar_tela():
  os.system("clear")

def mostra_exercicio(dia):
  return f"Exercicio do dia {dia}"

def exercicio1():
  print("========== Bem vindo ao sistema de cadastro =============")
  print("Digite o seu nome?")
  nome = input()
  print("Digite o seu telefone:")
  telefone = input()
  print("Digite o seu endereço:")
  endereco = input()

  os.system('clear')
  print("========== Programa de formatação de dados ==============")
  print("Nome: "+ nome)
  print("Telefone: "+ telefone)
  print("Endereço: "+ endereco)
  print("=========================================================")

def exercicio2():
  print("========== Sistema de combustível ===============")
  print("Digite a quantidade de litros padrão:")
  litroPosto = input()
  print("Digite a quantidade de litros para preencher a quantidade total:")
  atualPosto = input()

  print(f"A quantidade dque litros que ficou no posto foi: {atualPosto}")

  print(f":::: Chegou um cliente, bora vender? :::::")
  print(f"Digite o nome do cliente:")
  nomeConsumidor = input()
  print(f"Digite o valor que o senhor(a) {nomeConsumidor} que deseja colocar:")
  abastecer = input()

  resto = float(atualPosto) - float(abastecer)
  print(
      f"::: Ficou com {resto} litros de um total de {atualPosto} combustível no tanque do posto ::::")


def exercicio3():
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
      print(
          f"O resultado alcançado foi {somar_resultados} e ficou abaixo da expectativa")
      print("=========================")



while True:
  print("=== Bem vindo ao programa - RESUMO ===\n")
  print("Digite um opção:\n")
  for i in range(0, 3):
    print(f"{i+1} - {mostra_exercicio(i+1)}")
  print("10 - Sair do programa")

  opcao = int(input())

  if opcao == 10:
    break
  elif opcao == 1:
    limpar_tela()
    exercicio1()
  elif opcao == 2:
    limpar_tela()
    exercicio2()
  elif opcao == 3:
    limpar_tela()
    exercicio3()
  else:
   print("Em construção")
