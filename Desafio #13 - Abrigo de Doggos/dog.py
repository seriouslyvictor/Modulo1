class Doggo:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.brinquedo = None
    def latir(self):
        print(f"{self.nome} diz: Woof Woof 🐶 !!")
    def ___str___ (self):
        print(f"{self.nome} é um {self.raca} com {self.idade} anos de idade!")
    def buscar_osso(self):
        import random
        animais = ["boi", "galinha", "humano", "frango", "porco"]
        print(f"{self.nome} foi buscar um osso... ele voltou com belíssimo osso de {random.choice(animais)}!")
    def aniversario(self):
        self.idade += 1
        print(f"{self.nome} agora tem {self.idade} anos!")
    def brincar(self):
        if not self.brinquedo:
            print(f"{self.nome} sai correndo atrás do próprio rabo com muita energia!")
        else:
            print(r"""
     ██▄▄▄▄▄▄▄▄▄   
    ▒▒▒▒▒▒▒▒▒▒▓██  
   ▀▀▒▒▒▀▀▒▒▒▓▓▓▓█ 
 ▄▄▄▒▒░    ░░▒▒▒▓█ 
 ▀▀▀▒▄▄▄   ░░▒▒▒▓█ 
   █▄░   ░░▒▒▒▒▓▓█ 
    ▀█▄▄▄▄▄▄▄▄▄▀▀  
                    """)
            print(f"{self.nome} pega o seu {self.brinquedo} e sai brincando com muita energia!")

