import json
import os
import uuid


class Animal():
    def __init__(self, animal_dict={"codigo": "", "nome": "", "descricao": ""}):
        self.codigo = animal_dict["codigo"]
        self.nome = animal_dict["nome"]
        self.descricao = animal_dict["descricao"]

    def gravar(self):
        animais = Animal.buscar()
        animal_existe = any(a for a in animais if a.codigo == self.codigo)
        if animal_existe:
            return

        self.codigo = str(uuid.uuid4())
        animais.append(self)
        f = open(Animal.__caminho_arquivo(), "w")
        try:
            animais_json = json.dumps([obj.__dict__ for obj in animais])
            f.write(animais_json)
        except Exception as e:
            print(e)
            print("Algo deu errado na escrita do arquivo")
        finally:
            f.close()

    @staticmethod
    def buscar_por_codigo(codigo):
        animais = Animal.buscar()
        return next((a for a in animais if a.codigo == codigo), None)

    @staticmethod
    def buscar():
        Animal.__criar_db_se_nao_existe()
        f = open(Animal.__caminho_arquivo(), "r")
        try:
            return Animal.__converter_list_dict_objeto_animal(json.loads(f.read()))
        except:
            return []
        finally:
            f.close()

    ##### Métodos privados #####

    @staticmethod
    def __converter_list_dict_objeto_animal(animais_dict):
        animais = []
        for animal in animais_dict:
            animais.append(Animal(animal))
        return animais

    @staticmethod
    def __caminho_arquivo():
        caminho_arquivo = os.path.dirname(__file__)
        return f"{caminho_arquivo}/../db/animais.json"

    @staticmethod
    def __criar_db_se_nao_existe():
        from os.path import exists
        if not exists(Animal.__caminho_arquivo()):
            f = open(Animal.__caminho_arquivo(), "w")
            try:
                animais_json = json.dumps([])
                f.write(animais_json)
            except Exception as e:
                print(e)
                print("Algo deu errado na escrita do arquivo")
            finally:
                f.close()

