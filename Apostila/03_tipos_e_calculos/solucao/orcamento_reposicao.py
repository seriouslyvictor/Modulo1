# Calcula custo, caixas completas e unidades restantes de uma reposição.
nome_produto = input("Produto: ")
quantidade = int(input("Quantidade comprada: "))
preco_unitario = float(input("Preço unitário: "))
capacidade_caixa = int(input("Unidades por caixa: "))

custo_total = quantidade * preco_unitario
caixas_completas = quantidade // capacidade_caixa
unidades_restantes = quantidade % capacidade_caixa

print()
print("--- ORÇAMENTO ---")
print(f"Produto: {nome_produto}")
print(f"Custo total: R$ {custo_total:.2f}")
print(f"Caixas completas: {caixas_completas}")
print(f"Unidades restantes: {unidades_restantes}")

