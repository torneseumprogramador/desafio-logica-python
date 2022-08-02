import utils


def exercicio():
  utils.limpar_tela()
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
