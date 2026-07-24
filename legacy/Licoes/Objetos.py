class Doggo:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.idade = idade
        self.raca = raca
    def latir(self):
        print(f"{self.nome} diz: Woof Woof 🐶 !!")
    def descrever(self):
        print(f"{self.nome} é um {self.raca} com {self.idade} anos de idade!")
    def buscar_osso(self):
        import random
        animais = ["boi", "galinha", "humano", "frango", "porco"]
        print(f"{self.nome} foi buscar um osso... ele voltou com belíssimo osso de {random.choice(animais)}!")

dog1 = Doggo("Rex", "Pastor Alemão", 5)
dog2 = Doggo("Bella", "Labrador", 3)
dog3 = Doggo("TIBURCIO", "Fake Dog", 11)

dog1.latir()
dog1.descrever()

dog2.latir()
dog3.latir()
dog1.buscar_osso()

#Mini Desafios:
#Crie um novo métood chamado aniversario() que aumenta a idade do dog em 1 ano.
#A saida do método deve ser: "{nome do cachorro} está fazendo aniversário e agora tem {anos} anos de idade!"

#Crie um novo atributo chamado brinquedo_favorito, depois, crie um método chamado brincar() com a saida
#"{nome do cachorro} pega o seu {brinquedo} e o joga para o alto!"

#Perguntas para reflexão:
#O que acontece se esquecermos de passar um dos parâmetros ao criar um novo cachorro?
#Seria possível criar 10 cachorros rapidamente usando um Loop?