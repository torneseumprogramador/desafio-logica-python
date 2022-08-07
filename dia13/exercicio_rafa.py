"""
Jardeclenio é um empresário dono de um zoologico e precisa de um programa para cadastrar os seus animais.
Faça um programa que persista os dados dos animais no disco.
Exemplo do escopo da classe
Animal

# propriedades
-numero
-nome
-descricao
# metodos
# métodos internos da classe
 - gravar
 - buscar
 - mostrar

"""

from os.path import exists
import json
import os


class Cores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'


class Animal():

    def __init__(self):
        self.numero = 0
        self.nome = ""
        self.descricao = ""

    @staticmethod
    def __to_object(itens):
        lista = []
        for item in itens:
            animal = Animal()
            animal.numero = item["numero"]
            animal.nome = item["nome"]
            animal.descricao = item["descricao"]
            lista.append(animal)

        return lista

    @staticmethod
    def __campo_texto(label):
        while True:
            valor_input = input(f"Digite o valor para o campo {label}: ")
            if valor_input.strip() == "":
                print(
                    f"{Cores.WARNING}Alerta: Valor inválido. {label}{Cores.ENDC}")
                return Animal.__campo_texto(label)

            return valor_input

    @staticmethod
    def __campo_numerico(label):
        while True:
            valor_input = input(f"Digite o valor para o campo {label}: ")
            if valor_input.isnumeric() == False:
                print(
                    f"{Cores.WARNING}Alerta: Valor inválido. {label}{Cores.ENDC}")
                return Animal.__campo_numerico(label)

            return int(valor_input)

    def __formulario(self, exibe_cabecalho=True):
        if(exibe_cabecalho == True):
            print(
                f"{Cores.OKBLUE}============================[Cadastro de Animais]============================{Cores.ENDC}")

            try:

                self.numero = Animal.__gerar_numero()
                self.nome = Animal.__campo_texto("Nome")
                self.descricao = Animal.__campo_texto("Descrição")

                return self

            except TypeError as e:
                print(f"{Cores.WARNING}Alerta: {e}{Cores.ENDC}")
            except Exception as e:
                print(f"{Cores.FAIL}Erro: {e}{Cores.ENDC}")
                return None

    def cadastro(self):
        try:
            resultado = self.__formulario()

            if resultado == None:
                raise Exception(
                    "Não foi possível criar o objeto para cadastro.")

            if self.salvar_arquivo() == True:
                print(f"{Cores.OKGREEN}Animal cadastrado com sucesso.{Cores.ENDC}")

            while True:
                print("Deseja cadastar novo Animal ?")
                print("1 - Sim")
                print("2 - Não")
                print("0 - Retornar ao menu anterior")

                opcao_selecionada = Animal.obtem_opcao_menu(1, 2)
                if opcao_selecionada == 1:
                    resultado = self.__formulario()
                    if resultado != None:
                        if self.salvar_arquivo() == True:
                            print(
                                f"{Cores.OKGREEN}Animal cadastrado com sucesso.{Cores.ENDC}")

                if opcao_selecionada == 0 or opcao_selecionada == 2:
                    Animal.limpar_tela()
                    return True

        except Exception as e:
            print(f"{Cores.FAIL}Erro: {e}{Cores.ENDC}")
            return False

    @staticmethod
    def __obtem_todos_animais():
        lista = Animal.__ler_arquivo()
        try:
            return Animal.__to_object(lista)
        except:
            return []

    @staticmethod
    def __obtem_animais_por_numero(numero):
        lista = Animal.__obtem_todos_animais()
        return next((a for a in lista if a.numero == numero), None)

    @staticmethod
    def busca_animais_por_nome(numero):

        resultado = Animal.__obtem_animais_por_numero(numero)

        if resultado == None:
            print(
                f"{Cores.WARNING}Não foi encontrado nenhum animal com o número {numero} no sistema.{Cores.ENDC}")

        else:
            print(
                f"{Cores.OKBLUE}============================[Resultado de Animais]============================{Cores.ENDC}")

            print(f"Numero: {resultado.numero}")
            print(f"Nome: {resultado.nome}")
            print(f"Descricao: {resultado.descricao}")
            print(
                "------------------------------------------------------------------------------")

    @staticmethod
    def buscar():
        print(
            f"{Cores.OKBLUE}============================[Busca de Animais]============================{Cores.ENDC}")

        try:
            numero = Animal.__campo_numerico("Número")
            Animal.busca_animais_por_nome(numero)

        except TypeError as e:
            print(f"{Cores.WARNING}Alerta: {e}{Cores.ENDC}")
        except Exception as e:
            print(f"{Cores.FAIL}Erro: {e}{Cores.ENDC}")

    @staticmethod
    def relatorio():

        lista = Animal.__obtem_todos_animais()
        if len(lista) == 0:
            print(
                f"{Cores.WARNING}Não existe nenhum animal cadastrado no sistema.{Cores.ENDC}")

        else:
            print(
                f"{Cores.OKBLUE}============================[Relatório de Animais]============================{Cores.ENDC}")

            for item in lista:
                print(f"{Cores.CYELLOW2}Número: {item.numero}{Cores.ENDC}")
                print(f"{Cores.CYELLOW2}Nome: {item.nome}{Cores.ENDC}")
                print(f"{Cores.CYELLOW2}Descrição: {item.descricao}{Cores.ENDC}")
                print(
                    f"{Cores.OKBLUE}------------------------------------------------------------------------------{Cores.ENDC}")

    @staticmethod
    def __gerar_numero():

        try:
            lista = Animal.__ler_arquivo()
            if len(lista) == 0:
                return 1

            resultado = max(lista, key=lambda item: item["numero"])
            numero = int(resultado["numero"]) + 1
            return numero
        except Exception as e:
            print(f"{Cores.FAIL}Erro: {e}{Cores.ENDC}")

    @staticmethod
    def __criar_arquivo():
        try:
            path_arquivo_json = Animal.__path_arquivo()
            arquivo = open(path_arquivo_json, 'r')
        except FileNotFoundError:
            arquivo = open(path_arquivo_json, 'w')
            arquivo.write(json.dumps([]))
        finally:
            arquivo.close()

    @staticmethod
    def __ler_arquivo():
        try:
            path_arquivo_json = Animal.__path_arquivo()
            arquivo = exists(path_arquivo_json)
            if not arquivo:
                Animal.__criar_arquivo()

            arquivo = open(path_arquivo_json, "r")
            lista = arquivo.read()
            lista_json_loads = json.loads(lista)

            return lista_json_loads

        except Exception as e:
            print(f"{Cores.FAIL}Erro: {e}{Cores.ENDC}")

        finally:
            arquivo.close()

    @staticmethod
    def __path_arquivo():
        path_arquivo_json = os.path.dirname(__file__)
        return f"{path_arquivo_json}\zoologico.json"

    def salvar_arquivo(self):
        try:
            path_arquivo_json = Animal.__path_arquivo()
            arquivo = exists(path_arquivo_json)
            if not arquivo:
                Animal.__criar_arquivo()

            animais = Animal.__obtem_todos_animais()
            animais.append(self)

            arquivo = open(path_arquivo_json, "w")
            json_string = json.dumps([obj.__dict__ for obj in animais])

            arquivo.write(json_string)

        except Exception as e:
            print(f"{Cores.FAIL}Erro: {e}{Cores.ENDC}")
            return False
        finally:
            arquivo.close()
            return True

    @staticmethod
    def obtem_opcao_menu(incial, final):

        try:

            valor_convertido = Animal.__campo_numerico("Menu")

            if valor_convertido == 0:
                return 0
            elif valor_convertido >= incial and valor_convertido <= final:
                return valor_convertido
            else:
                raise TypeError("Opção inválida.")
        except TypeError as e:
            print(f"{Cores.WARNING}Alerta: {e}{Cores.ENDC}")
            return Animal.obtem_opcao_menu(incial, final)

    @staticmethod
    def limpar_tela():
        os.system("cls" if os.name == "nt" else "clear")


def main():
    animal = Animal()

    while True:
        print(
            f"{Cores.OKBLUE}============================[Sistema do Zoológico]============================{Cores.ENDC}")
        print(f"{Cores.OKBLUE}1 - Cadastro{Cores.ENDC}")
        print(f"{Cores.OKBLUE}2 - Buscar{Cores.ENDC}")
        print(f"{Cores.OKBLUE}3 - Relatório{Cores.ENDC}")
        print(f"{Cores.OKBLUE}4 - Sair do programa{Cores.ENDC}")
        print(f"{Cores.OKBLUE}=============================================================================={Cores.ENDC}")

        menu = Animal.obtem_opcao_menu(1, 5)

        if menu == 1:
            # Cadastro de Cliente
            Animal.limpar_tela()
            animal.cadastro()

        elif menu == 2:
            # Buscar
            Animal.limpar_tela()
            Animal.buscar()

        elif menu == 3:
            # Relatório
            Animal.limpar_tela()
            Animal.relatorio()
        elif menu == 4:
            print("Sair do programa")
            break


main()