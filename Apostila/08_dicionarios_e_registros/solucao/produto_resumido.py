produto = {"nome": "Caderno", "preco": 8.50, "quantidade": 4}
produto["categoria"] = "Papelaria"
produto["quantidade"] = 6

valor_total = produto["preco"] * produto["quantidade"]

for chave, valor in produto.items():
    print(f"{chave}: {valor}")

print(f"Valor total: R$ {valor_total:.2f}")

