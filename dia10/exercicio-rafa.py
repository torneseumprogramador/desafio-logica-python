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

# https://github.com/rhsilva06/Desafio21DiasPython/blob/main/exercicio10.py

import os
import re

lista_clientes = []
lista_produtos = []
lista_pedidos = []


def isfloat(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def valida_email(email):
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if re.match(regex, email):
        return True
    return False


def gerar_relatorio(clientes, produtos, pedidos, exibecabecalho=True):
    try:
        if exibecabecalho == True:
            mostrar_lista_relatorio()

        opcao_selecionada = obtem_opcao_menu(1, 3)
        if opcao_selecionada == 1:
            relatorio_cliente(clientes)
        elif opcao_selecionada == 2:
            relatorio_produto(produtos)
        elif opcao_selecionada == 3:
            relatorio_pedido(pedidos)

        print("Deseja gerar mais algum relatório ?")
        print("1 - Sim")
        print("2 - Não")
        opcao_selecionada = obtem_opcao_menu(1, 2)
        if opcao_selecionada == 1:
            return gerar_relatorio(clientes, produtos, pedidos, exibecabecalho=False)
        if opcao_selecionada == 2:
            return
    except Exception as e:
        print(f"Alerta: {e}")


def cadastro_cliente(lista, nome="", email="", exibe_cabecalho=True):

    if(exibe_cabecalho == True):
        print(
            "============================[Cadastro de Clientes]============================")

    try:

        if nome.strip() == "":
            nome = input("Digite o nome do Cliente: ")
            if nome.strip() == "":
                raise TypeError("Digite o nome do Cliente corretamente.")

        email = input("Digite o e-mail do Cliente: ")
        if email.strip() == "":
            raise TypeError("Digite o e-mail do Cliente corretamente.")

        if valida_email(email) == False:
            raise TypeError("Digite o e-mail do Cliente corretamente.")

        if busca_cliente(lista, email) != None:
            raise TypeError("E-mail já cadastrado.")

        resultado = cria_item_cliente(lista_clientes, nome, email)
        lista.append(resultado)

        while True:
            print("Deseja cadastar novo Cliente ?")
            print("1 - Sim")
            print("2 - Não")
            print("0 - Retornar ao menu anterior")

            opcao_selecionada = obtem_opcao_menu(1, 2)

            if opcao_selecionada == 1:
                nome = ""
                email = ""
                exibe_cabecalho = True
                limpar_tela()

            if opcao_selecionada == 0 or opcao_selecionada == 2:
                limpar_tela()
                return lista

            return cadastro_cliente(lista, nome, email, exibe_cabecalho)
    except Exception as e:
        print(f"Alerta: {e}")
        return cadastro_cliente(lista, nome, email, exibe_cabecalho=False)


def cadastro_produto(lista, nome_produto="", descricao="", preco="", exibe_cabecalho=True):
    if(exibe_cabecalho == True):
        print(
            "============================[Cadastro de Produtos]============================")

    try:
        if nome_produto.strip() == "":
            nome_produto = input("Digite o nome do produto: ")
            if nome_produto.strip() == "":
                raise TypeError("Digite o nome do produto corretamente.")

        if obtem_produto(lista, nome_produto) != None:
            nome_produto = ""
            raise TypeError("Produto já cadastrado.")

        if descricao.strip() == "":
            descricao = input("Digite a descrição do produto: ")
            if descricao.strip() == "":
                raise TypeError("Digite a descrição do produto corretamente.")

        preco = input("Digite o preço do produto: ")
        # if preco.isnumeric() == False:
        if isfloat(preco) == False:
            raise TypeError("Digite o preço do produto corretamente.")

        resultado = cria_item_produto(
            lista_produtos, nome_produto, descricao, preco)
        lista.append(resultado)

        while True:
            print("Deseja cadastar novo Produto ?")
            print("1 - Sim")
            print("2 - Não")
            print("0 - Retornar ao menu anterior")

            opcao_selecionada = obtem_opcao_menu(1, 2)
            if opcao_selecionada == 1:
                nome_produto = ""
                descricao = ""
                preco = ""
                exibe_cabecalho = True
                limpar_tela()

            if opcao_selecionada == 0 or opcao_selecionada == 2:
                limpar_tela()
                return lista

            return cadastro_produto(lista, nome_produto, descricao, preco, exibe_cabecalho)

    except Exception as e:
        print(f"Alerta: {e}")
        return cadastro_produto(lista, nome_produto, descricao, preco, exibe_cabecalho=False)


def cadastro_pedido(pedidos, clientes, produtos, exibe_cabecalho=True):
    if exibe_cabecalho == True:
        print(
            "============================[Cadastro de Pedidos]============================")

    try:
        if len(clientes) == 0:
            raise TypeError(
                "Para fazer cadastro de pedido é necessário ter clientes cadastrados.")
        if len(produtos) == 0:
            raise TypeError(
                "Para fazer cadastro de pedido é necessário ter produtos cadastrados.")

        cliente = obtem_cliente(clientes)
        print(f"Cliente {cliente['nome']}")

        print(
            "============================[Lista de Produtos]============================")

        mostrar_lista_produto(produtos)
        itens = obtem_lista_pedido(produtos, cliente)

        if itens == None or len(itens) == 0:
            raise TypeError("Nenhum produto vinculado ao pedido.")

        resultado = cria_item_pedido(pedidos, cliente, itens)
        pedidos.append(resultado)

    except Exception as e:
        print(f"Alerta: {e}")
        return cadastro_pedido(pedidos, clientes, produtos, exibe_cabecalho=False)


def gerar_id(lista):
    id = len(lista) + 1
    return id


def obtem_produto(lista, nome_produto):
    return next((x for x in lista if x["nome_produto"] == nome_produto), None)


def busca_cliente(lista, valor):
    return next((x for x in lista if x["nome"] == valor or x["email"] == valor), None)


def obtem_cliente(lista):
    try:
        email = input("Digite e-mail do cliente: ")
        if email.strip() == "":
            raise TypeError("Alerta: Digite o e-mail do cliente.")

        if valida_email(email) == False:
            raise TypeError("Digite o e-mail do Cliente corretamente.")

        cliente = busca_cliente(lista, email)
        if cliente == None:
            raise TypeError("Alerta: Cliente não encontrado.")

        return cliente

    except TypeError as e:
        print(f"Alerta: {e}")
        return obtem_cliente(lista)


def cria_item_cliente(lista, nome, email):
    try:
        # gerar id do cliente
        id = gerar_id(lista)

        dict_cliente = {
            "id_cliente": id,
            "nome": nome,
            "email": email
        }
        return dict_cliente
    except Exception as e:
        print(f"Erro: {e}")


def cria_item_produto(lista, nome_produto, descricao, preco):
    try:
        id = gerar_id(lista)
        dict_produto = {
            "id_produto": id,
            "nome_produto": nome_produto,
            "descricao": descricao,
            "preco": preco
        }
        return dict_produto
    except Exception as e:
        print(f"Erro: {e}")


def cria_item_pedido(lista, cliente, itens):
    try:
        # gerar id do pedido
        id = gerar_id(lista)
        dict_pedido = {
            "id_pedido": id,
            "cliente": cliente,
            "itens": itens
        }

        return dict_pedido
    except Exception as e:
        print(f"Erro: {e}")


def mostrar_lista_relatorio():
    print(
        "============================[Relatórios]============================")
    print(" 1 - Relatório de Clientes")
    print(" 2 - Relatório de Produtos")
    print(" 3 - Relatório de Pedidos")
    print(" 0 - Retornar o menu anterior")


def obtem_opcao_menu(incial, final):

    try:
        valor_entrada = input('Digite a opção: ')

        if valor_entrada.isnumeric() == False:
            raise TypeError("Opção inválida.")

        valor_convertido = int(valor_entrada)
        if valor_convertido == 0:
            return 0
        elif valor_convertido >= incial and valor_convertido <= final:
            return valor_convertido
        else:
            raise TypeError("Opção inválida.")
    except TypeError as e:
        print(f"Alerta: {e}")
        return obtem_opcao_menu(incial, final)


def mostrar_lista_produto(lista):
    for item in lista:
        print(
            f"{item['id_produto']} - {item['nome_produto']} - {item['descricao']} - {item['preco']}")


def obtem_lista_pedido(lista, cliente):
    itens = []
    try:
        while True:
            nome_produto = input('Digite o nome do produto: ')
            if nome_produto.strip() == "":
                raise TypeError("Digite o nome do produto.")

            produto = obtem_produto(lista, nome_produto)
            if produto == None:
                raise TypeError("Produto não encontrado.")

            itens.append(produto)

            print(
                f"Deseja fazer um novo pedido para o cliente {cliente['nome']} ?")
            print("1 - Sim")
            print("2 - Não")

            opcao_selecionada = obtem_opcao_menu(1, 2)
            if opcao_selecionada == 0 or opcao_selecionada == 2:
                return itens
    except TypeError as e:
        print(f"Alerta: {e}")
        return obtem_lista_pedido(lista, cliente)


def relatorio_cliente(lista):
    try:
        if len(lista) == 0:
            print("Nenhum cliente cadastrado para gerar o relatório.")
            return

        print(
            "============================[Relatório de Clientes]============================")
        for item in lista:
            print(f"Id: {item['id_cliente']}")
            print(f"Nome: {item['nome']}")
            print(f"E-mail: {item['email']}")
            print(
                "-------------------------------------------------------------------------------")

    except Exception as e:
        print(f"Erro: {e}")


def relatorio_produto(lista):
    try:
        if len(lista) == 0:
            print("Nenhum produto cadastrado para gerar o relatório.")
            return

        print(
            "============================[Relatório de Produtos]============================")
        for item in lista:
            print(f"Id: {item['id_produto']}")
            print(f"Nome produto: {item['nome_produto']}")
            print(f"Descrição: {item['descricao']}")
            print(f"Preço: {item['preco']}")
            print(
                "-------------------------------------------------------------------------------")
    except Exception as e:
        print(f"Erro: {e}")


def relatorio_pedido(lista):
    try:
        if len(lista) == 0:
            print("Nenhum pedido cadastrado para gerar o relatório.")
            return

        print(
            "============================[Relatório de Pedidos]============================")
        for item in lista:
            print(f"Id: {item['id_pedido']}")
            print(f"Cliente: {item['cliente']['nome']}")
            print(f"Pedido(s) quantidade : {len(item['itens'])}")
            soma = 0
            for produto in item["itens"]:
                print(f"Nome produto: {produto['nome_produto']}")
                print(f"Descrição: {produto['descricao']}")
                print(f"Preço: {produto['preco']}")
                soma += float(produto['preco'])
            print('Total: {:0.2f}'.format(soma))
            print(
                "-------------------------------------------------------------------------------")
    except Exception as e:
        print(f"Erro: {e}")


def main():
    while True:
        print(
            "============================[Sistema de Pedidos]============================")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Produto")
        print("3 - Cadastrar Pedido")
        print("4 - Relatórios")
        print("5 - Sair do programa")
        print(
            "============================================================================")

        menu = obtem_opcao_menu(1, 5)

        if menu == 1:
            # Cadastro de Cliente
            limpar_tela()
            cadastro_cliente(lista_clientes)

        elif menu == 2:
            # Cadastro de Produtos
            limpar_tela()
            cadastro_produto(lista_produtos)

        elif menu == 3:
            # Cadastro de Pedido
            limpar_tela()
            cadastro_pedido(lista_pedidos, lista_clientes, lista_produtos)
        elif menu == 4:
            # relatórios
            limpar_tela()
            gerar_relatorio(lista_clientes, lista_produtos, lista_pedidos)

        elif menu == 5:
            print("Sair do programa")
            break


main()
