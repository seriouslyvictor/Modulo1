# Calcula o custo de um lote para reposição do estoque.
print("=== CUSTO DE REPOSIÇÃO ===")

nome_produto = input("Produto: ")
quantidade = int(input("Quantidade comprada: "))
preco_unitario = float(input("Preço unitário: "))

custo_lote = quantidade * preco_unitario

print()
print("--- RESUMO DA REPOSIÇÃO ---")
print(f"Produto: {nome_produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Custo do lote: R$ {custo_lote:.2f}")

