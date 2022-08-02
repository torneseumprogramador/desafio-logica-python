import utils


def exercicio():
  utils.limpar_tela()
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

