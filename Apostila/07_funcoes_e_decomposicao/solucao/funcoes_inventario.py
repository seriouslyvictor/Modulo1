def calcular_custo(quantidade, preco_unitario):
    return quantidade * preco_unitario


def classificar_estoque(quantidade, estoque_minimo):
    if quantidade < 0 or estoque_minimo < 0:
        return "inválido"
    if quantidade == 0:
        return "esgotado"
    if quantidade <= estoque_minimo:
        return "crítico"
    return "adequado"


def exibir_resumo(nome, quantidade, custo, situacao):
    print(f"Produto: {nome}")
    print(f"Quantidade: {quantidade}")
    print(f"Custo: R$ {custo:.2f}")
    print(f"Situação: {situacao}")


nome_produto = "Caderno"
quantidade_produto = 3
preco_produto = 8.50
minimo_produto = 5

custo_produto = calcular_custo(quantidade_produto, preco_produto)
situacao_produto = classificar_estoque(quantidade_produto, minimo_produto)
exibir_resumo(nome_produto, quantidade_produto, custo_produto, situacao_produto)

