class Categoria:
    def __init__(self, nome):
        if not nome:
            raise ValueError("O nome é obrigatório.")
        self.nome = nome

    def renomear(self, novo_nome):
        if not novo_nome:
            raise ValueError("O novo nome é obrigatório.")
        self.nome = novo_nome

    def __str__(self):
        return self.nome


def main():
    papelaria = Categoria("Papelaria")
    higiene = Categoria("Higiene")
    papelaria.renomear("Material escolar")

    print(papelaria)
    print(higiene)


if __name__ == "__main__":
    main()

