import calculos


def main():
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    capacidade = int(input("Unidades por caixa: "))

    custo = calculos.calcular_custo(quantidade, preco)
    caixas = calculos.calcular_caixas(quantidade, capacidade)
    sobra = calculos.calcular_sobra(quantidade, capacidade)

    print(f"Custo: R$ {custo:.2f}")
    print(f"Caixas completas: {caixas}")
    print(f"Unidades restantes: {sobra}")


if __name__ == "__main__":
    main()

