import regras_estoque


def main():
    nome = input("Produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    minimo = int(input("Estoque mínimo: "))

    valor = regras_estoque.calcular_valor(quantidade, preco)
    situacao = regras_estoque.classificar(quantidade, minimo)

    print(f"{nome}: R$ {valor:.2f} — {situacao}")


if __name__ == "__main__":
    main()

