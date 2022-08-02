import utils


def exercicio():
  utils.limpar_tela()
  print("========== Bem vindo ao sistema de cadastro =============")
  print("Digite o seu nome?")
  nome = input()
  print("Digite o seu telefone:")
  telefone = input()
  print("Digite o seu endereço:")
  endereco = input()

  utils.limpar_tela()

  print("========== Programa de formatação de dados ==============")
  print("Nome: "+ nome)
  print("Telefone: "+ telefone)
  print("Endereço: "+ endereco)
  print("=========================================================")

if __name__ == "__main__" :
  exercicio()
