produtos = ["Caderno", "Caneta"]
print(f"Lista inicial: {produtos}")
print(f"Tamanho inicial: {len(produtos)}")

produtos.append("Borracha")
produtos.insert(1, "Lápis")
produtos[0] = "Caderno universitário"

if "Caneta" in produtos:
    produtos.remove("Caneta")

produtos.sort()
print(f"Primeiro: {produtos[0]}")
print(f"Último: {produtos[-1]}")
print(f"Tamanho final: {len(produtos)}")
print(produtos)

