''''
Faca um programa para calcular os valores de um pedido
para isso crie um objeto dict de pedido que tenha relacao com um objeto dict de cliente

pedido = {
    "id": 1,
    "cliente": {
        "nome": "Walter"
    },
    "itens": []
}

nesse pedido, coloque uma propriedade de itens, contendo instancias de um dict de produto
no pedido, crie uma função para calcular o valor total
e uma função para mostrar um relatório do pedido, mostrando da seguinte forma:
----------------------------------------------------------------
Pedido Id: 1
Nome: João
Valor Total: R$ 999,99
----------------------------------------------------------------
O que terá no dict de pedido:
- id
- cliente
- itens []
O que terá no dict cliente:
- Nome
- email
O que terá no dict produto:
- Nome
- descrição
- preço
'''

# https://github.com/Jo-Alves/exercicio-python-dia10.git

import os
import time

valor_total = 0

def Calcular_Valor_Total(interator=0):
    if interator == len(pedidos):
        return
    
    for item in pedidos[interator]["itens"]:
        preco = item["preco"]
        global valor_total
        valor_total += preco

    pedidos[interator]["valor_total"] = valor_total
    valor_total = 0
    Calcular_Valor_Total(interator + 1)

def mostrar_relatorio():
    Calcular_Valor_Total()   
    print("==================== [RELATÓRIO DE PEDIDOS] ====================")
    for pedido in pedidos:
        print(f"Pedido nº: {pedido['id']}")
        print(f"Cliente: {pedido['cliente']['nome']}")
        print("Valor total: {:.2f}".format(pedido['valor_total']))
        print("================================================")
   
pedidos = []

def gerar_pedido():
    try:
        id = 0
        while True:
            id += 1
            pedido = {}
            pedido["id"] = id
            pedido["cliente"] = {}
            pedido["cliente"]["nome"] = input("Digite o nome do cliente:\n")
            pedido["cliente"]["email"] = input("Digite o email do cliente:\n")
            os.system("clear" if "clear" else "cls")
            pedido["itens"] = []
            while True:
                produto = {}
                produto["nome"] = input("Digite o nome do produto:\n")
                produto["descricao"] = input("Digite a descrição do produto:\n")
                produto["preco"] = float(input("Digite o preço do produto:\n"))
                pedido["itens"].append(produto)
                tecla = (input("Aperte a tecla '0' para continuar inserindo produto para o pedido\n"))
                if(tecla != "0"):
                    break

            pedidos.append(pedido)
            decisao = input("Deseja gerar um novo pedido? (S|N): ")
            if(decisao.lower() != 's'):
                os.system("clear" if "clear" else "cls")
                mostrar_relatorio()
                time.sleep(0.3)
                break
    except Exception as ex:
        print(f"Digite um valor válido para o preço\nExceção'{ex}'")


gerar_pedido()
