produtos = [
    {"nome": "Caderno", "categoria": "Papelaria", "preco": 8.50, "quantidade": 10, "estoque_minimo": 3},
    {"nome": "Caneta", "categoria": "Papelaria", "preco": 3.20, "quantidade": 0, "estoque_minimo": 5},
    {"nome": "Sabonete", "categoria": "Higiene", "preco": 4.00, "quantidade": 2, "estoque_minimo": 4},
    {"nome": "Café", "categoria": "Alimentos", "preco": 18.00, "quantidade": 6, "estoque_minimo": 2},
]

valor_catalogo = 0
reposicoes = 0

for produto in produtos:
    valor_produto = produto["preco"] * produto["quantidade"]
    valor_catalogo += valor_produto

    if produto["quantidade"] == 0:
        situacao = "esgotado"
        reposicoes += 1
    elif produto["quantidade"] <= produto["estoque_minimo"]:
        situacao = "crítico"
        reposicoes += 1
    else:
        situacao = "adequado"

    print(f"{produto['nome']} — {produto['categoria']}")
    print(f"Quantidade: {produto['quantidade']} — {situacao}")
    print(f"Valor: R$ {valor_produto:.2f}")

print(f"Valor total do catálogo: R$ {valor_catalogo:.2f}")
print(f"Produtos para reposição: {reposicoes}")

