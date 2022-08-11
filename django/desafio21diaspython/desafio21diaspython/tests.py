from django.test import TestCase

class Animal():
    def __init__(self):
        self.nome = ""
        self.descricao = ""

    def falar(self):
        return f"Nome: {self.nome}, Descrição: {self.descricao}"

class AnimalTest(TestCase):
    def setUp(self):
        print("--[Roda antes do teste]--")

    def test_animais_podem_falar(self):
        animal = Animal()
        animal.nome = "Leão"
        animal.descricao = "Rei da selva"

        self.assertEqual(animal.falar(), 'Nome: Leão, Descrição: Rei da selva')