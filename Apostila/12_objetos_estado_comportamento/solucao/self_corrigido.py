class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


caderno = Produto("Caderno", 8.50, 10)
print(caderno.nome)

