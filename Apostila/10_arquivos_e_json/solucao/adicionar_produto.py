import json

with open("produtos.json", mode="r", encoding="utf-8") as arquivo:
    produtos = json.load(arquivo)

produto = {
    "nome": input("Nome: "),
    "categoria": input("Categoria: "),
    "preco": float(input("Preço: ")),
    "quantidade": int(input("Quantidade: ")),
}
produtos.append(produto)

with open("produtos.json", mode="w", encoding="utf-8") as arquivo:
    json.dump(produtos, arquivo, ensure_ascii=False, indent=2)

print(f"Produtos cadastrados: {len(produtos)}")

