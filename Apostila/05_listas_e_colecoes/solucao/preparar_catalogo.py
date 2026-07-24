produtos = ["Caderno", "Caneta", "Borracha"]

novo_produto = input("Novo produto: ")
produtos.append(novo_produto)

produto_remover = input("Produto para remover: ")
if produto_remover in produtos:
    produtos.remove(produto_remover)
else:
    print("Produto não encontrado.")

produtos.sort()
print(f"Quantidade: {len(produtos)}")
print(f"Primeiro: {produtos[0]}")
print(f"Último: {produtos[-1]}")
print(f"Catálogo: {produtos}")

