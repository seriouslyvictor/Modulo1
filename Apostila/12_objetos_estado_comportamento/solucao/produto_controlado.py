class Produto:
    def __init__(self, nome, preco, quantidade, estoque_minimo):
        if not nome:
            raise ValueError("Nome obrigatório.")
        if preco <= 0 or quantidade < 0 or estoque_minimo < 0:
            raise ValueError("Dados numéricos inválidos.")
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

    def adicionar(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Entrada inválida.")
        self.quantidade += quantidade

    def remover(self, quantidade):
        if quantidade <= 0 or quantidade > self.quantidade:
            raise ValueError("Saída inválida.")
        self.quantidade -= quantidade

    def __str__(self):
        return f"{self.nome}: {self.quantidade} — {self.classificar_estoque()}"


def main():
    produtos = [
        Produto("Caderno", 8.50, 10, 3),
        Produto("Caneta", 3.20, 2, 5),
        Produto("Borracha", 2.50, 0, 2),
    ]

    produtos[0].adicionar(2)
    produtos[1].remover(1)

    for produto in produtos:
        print(produto)
        print(f"Valor: R$ {produto.valor_estoque():.2f}")

    try:
        produtos[2].remover(1)
    except ValueError as erro:
        print(f"Operação recusada: {erro}")


if __name__ == "__main__":
    main()

