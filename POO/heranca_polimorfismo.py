from dis import dis


class Dispositivo():
    def __init__(self):
        self.nome = ""
        self.chip = ""

    def ligar(self):
        return f"Estou ligando o dispositivo #{self.nome}"

    def desligar(self):
        return f"Estou desligando o dispositivo #{self.nome} do chip {self.chip}"


# dispo = Dispositivo()
# dispo.nome = "0059X"
# dispo.chip = "Intel"
# print(dispo.ligar())
# print(dispo.desligar())


class Celular(Dispositivo):
    def __init__(self):
        self.capa = ""
        self.cor = ""
        self.botoes = []

    def ligar(self):
        ligar_base_class = Dispositivo.ligar(self)
        return f"Estou ligando o celular com a capa ({self.capa}) nos botões ({self.botoes_formatados()}) - {ligar_base_class}"
    
    def botoes_formatados(self, param=""):
        return  param + "----" + ', '.join(self.botoes)


cel = Celular()
cel.capa = "preta"
cel.nome = "0059X"
cel.chip = "Intel"
print(cel.ligar())
print(cel.botoes_formatados("sddssds"))
print(cel.desligar())
