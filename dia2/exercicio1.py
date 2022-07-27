# Dados que o professor Danilo, precise mostrar algumas informações 
# importantes na tela, faça um programa que capture estas informações
# e mostre na tela de forma organizada, exemplo de organização:

# ========== Programa de formatação de dados ==============
# Nome: XXXXXX
# Telefone: XXXXXXX
# Endereço: XXXXXXX
# =========================================================
import os

print("================ Bem vindo ao sistema de cadastro =================")
print("Digite o seu nome:")
nome = input()
print("Digite o seu telefone:")
telefone = input()
print("Digite o seu endereço:")
endereco = input()

os.system('clear')

print("========== Programa de formatação de dados ==============")
print("Nome: " + nome)
print("Telefone: " + telefone)
print("Endereço: " + endereco)
print("=========================================================")