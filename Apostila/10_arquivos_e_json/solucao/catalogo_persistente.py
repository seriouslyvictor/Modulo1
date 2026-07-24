import json

with open("produtos.json", mode="r", encoding="utf-8") as arquivo:
    produtos = json.load(arquivo)

for produto in produtos:
    print(f"{produto['nome']}: {produto['quantidade']}")

novo_produto = {
    "nome": "Borracha",
    "categoria": "Papelaria",
    "preco": 2.50,
    "quantidade": 8,
}
produtos.append(novo_produto)

with open("produtos.json", mode="w", encoding="utf-8") as arquivo:
    json.dump(produtos, arquivo, ensure_ascii=False, indent=2)

print(f"Produtos salvos: {len(produtos)}")

