def calcular_valor_estoque(quantidade, preco):
    return quantidade * preco


def classificar_estoque(quantidade, minimo):
    if quantidade < 0 or minimo < 0:
        return "inválido"
    if quantidade == 0:
        return "esgotado"
    if quantidade <= minimo:
        return "crítico"
    return "adequado"


def exibir_resumo(nome, quantidade, valor, situacao):
    print(f"Produto: {nome}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor em estoque: R$ {valor:.2f}")
    print(f"Situação: {situacao}")


nome = input("Produto: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preço: "))
minimo = int(input("Estoque mínimo: "))

valor = calcular_valor_estoque(quantidade, preco)
situacao = classificar_estoque(quantidade, minimo)
exibir_resumo(nome, quantidade, valor, situacao)

