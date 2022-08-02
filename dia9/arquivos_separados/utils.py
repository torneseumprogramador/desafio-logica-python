import os
import time


def espera_em_segundos(segundos):
  time.sleep(segundos)

def limpar_tela():
  os.system("clear")

def mostra_exercicio(dia):
  return f"Exercicio do dia {dia}"
