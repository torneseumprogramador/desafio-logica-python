"""
O professor Danilo, necessita organizar os exercicios passados no desafio
de python, com isso deseja que seus alunos faça um programa utilizando
funções para organizar todos os exercícios passados em um menu.
Ou seja, crie um program que organize os exercicos em funções
dos dias 2,3,4,5,6,7,8
e acesse o exercicio através de uma organização em menu

neste exercicio quero que vcs chamem os arquivos originais depois 
de ser refatorado em funçoes
"""

import importlib.util
import os
import sys


def importa_funcao(pasta, *arquivos):
  modulos = []
  for arquivo in arquivos:
    file_path = os.path.join(os.path.dirname(__file__), f"../{pasta}/{arquivo}")
    foo_spec = importlib.util.spec_from_file_location(pasta, file_path)
    foo_module = importlib.util.module_from_spec(foo_spec)
    sys.modules[pasta] = foo_module
    foo_spec.loader.exec_module(foo_module)
    modulos.append(sys.modules[pasta])
  return modulos

funcoes = importa_funcao("dia2", "exercicio1.py")
for funcao in funcoes:
  funcao.exec()

# funcoes = importa_funcao("dia3", "exercicio1.py", "exercicio2.py", "exercicio3.py")
# for funcao in funcoes:
#   funcao.exec()
