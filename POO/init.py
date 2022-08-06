class Celular():
    def __init__(self):
        self.capa = ""
        self.cor = ""
        self.botoes = []

    def ligar(self):
        return f"Estou ligando o celular com a capa ({self.capa}) nos botões ({self.botoes_formatados()})"
    
    def botoes_formatados(self):
        return ', '.join(self.botoes)

sansung = Celular()
sansung.capa = "B3G-ttt"
sansung.cor = "Preta"
sansung.botoes = ["Ligar", "Volume UP", "Volume Down"]
print(sansung.ligar())

lg = Celular()
lg.capa = "KG-ttt"
lg.cor = "Azul"
lg.botoes = ["Ligar", "Volume UP", "Volume Down"]
print(lg.ligar())

iphone = Celular()
iphone.capa = "IP-ttt"
iphone.cor = "Prata"
iphone.botoes = ["Ligar", "Volume UP", "Volume Down", "Home"]
print(iphone.ligar())

x = ""
