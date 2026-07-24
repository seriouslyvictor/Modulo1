class Produto:
    def __init__(self, nome, preco, quantidade, estoque_minimo):
        if not nome:
            raise ValueError("O nome é obrigatório.")
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        if quantidade < 0 or estoque_minimo < 0:
            raise ValueError("Quantidades não podem ser negativas.")

        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.estoque_minimo = estoque_minimo

    def valor_estoque(self):
        return self.preco * self.quantidade

    def classificar_estoque(self):
        if self.quantidade == 0:
            return "esgotado"
        if self.quantidade <= self.estoque_minimo:
            return "crítico"
        return "adequado"

    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A entrada deve ser maior que zero.")
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A saída deve ser maior que zero.")
        if quantidade > self.quantidade:
            raise ValueError("Estoque insuficiente.")
        self.quantidade -= quantidade

    def __str__(self):
        return f"{self.nome} — {self.quantidade} unidades — R$ {self.preco:.2f}"


caderno = Produto("Caderno", 8.50, 10, 3)
caneta = Produto("Caneta", 3.20, 2, 5)

caderno.adicionar_estoque(5)
caneta.remover_estoque(1)

print(caderno)
print(caderno.classificar_estoque())
print(caneta)
print(caneta.classificar_estoque())

try:
    caneta.remover_estoque(10)
except ValueError as erro:
    print(f"Operação recusada: {erro}")

