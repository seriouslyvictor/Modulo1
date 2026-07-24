produto = {
    "nome": "Caderno",
    "preco": 8.50,
    "quantidade": 12,
    "ativo": True,
}

print(produto["nome"])
print(produto["quantidade"])

produto["quantidade"] = 15
produto["categoria"] = "Papelaria"
produto["localizacao"] = "Prateleira A"
produto["fornecedor"] = {"nome": "Papel & Cia", "cidade": "Campinas"}

print(produto.get("codigo_externo", "Não informado"))

for chave, valor in produto.items():
    print(f"{chave}: {valor}")

valor_estoque = produto["preco"] * produto["quantidade"]
print(f"Valor em estoque: R$ {valor_estoque:.2f}")
print(f"Cidade do fornecedor: {produto['fornecedor']['cidade']}")

