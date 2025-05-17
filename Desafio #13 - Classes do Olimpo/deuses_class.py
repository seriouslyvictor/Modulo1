class Deus:
    def __init__(self, nome, dominio, simbolo):
        self.nome = nome
        self.dominio = dominio
        self.simbolo = simbolo
        self.followers = 0

    def apresentar(self):
        print(f"Eu sou {self.nome}, deus do(a) {self.dominio}. Meu símbolo é {self.simbolo}.")

    def realizar_milagre(self):
        print(f"{self.nome} realiza um milagre divino relacionado ao(à) {self.dominio}!")
    def adicionar_seguidores(self, num):
        self.followers += num
    def __str__(self):
        return f"{self.nome}, Deus do {self.dominio}"


class Olimpo:
    def __init__(self):
        self.deuses = []

    def adicionar_deus(self, deus):
        self.deuses.append(deus)
        print(f"{deus.nome} subiu ao Monte Olimpo!")

    def mostrar_deuses(self):
        print("\n🌄 Deuses presentes no Olimpo:")
        for deus in self.deuses:
            print(f"- {deus.nome} ({deus.dominio})")

    def todos_os_milagres(self):
        print("\n⚡ Os deuses mostram seus poderes divinos:")
        for deus in self.deuses:
            deus.realizar_milagre()
    def maior_deus(self):
        if len(self.deuses) <= 0:
            print("Nenhum deus está no Olimpo...")
            return
            
        max_god = self.deuses[0]
        for deus in self.deuses:
            if deus.followers > max_god.followers:
                mais_adorado = deus
        print(f"O maior Deus do Olimpo atualmente é: {max_god}")




# Teste
zeus = Deus("Zeus", "Céu", "Raio")
poseidon = Deus("Poseidon", "Mar", "Tridente")
atena = Deus("Atena", "Sabedoria", "Coruja")

olimpo = Olimpo()
olimpo.adicionar_deus(zeus)
olimpo.adicionar_deus(poseidon)
olimpo.adicionar_deus(atena)

olimpo.mostrar_deuses()
olimpo.todos_os_milagres()

zeus.adicionar_seguidores(500)
atena.adicionar_seguidores(100)
olimpo.maior_deus()
