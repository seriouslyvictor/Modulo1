produtos = ["Caderno", "Caneta", "Borracha", "Lápis", "Régua"]
quantidades = [10, 0, 3, 7, 1]
estoque_minimo = 3

total_unidades = 0
esgotados = 0
criticos = 0
adequados = 0

for indice in range(len(produtos)):
    produto = produtos[indice]
    quantidade = quantidades[indice]
    total_unidades += quantidade

    if quantidade == 0:
        situacao = "esgotado"
        esgotados += 1
    elif quantidade <= estoque_minimo:
        situacao = "crítico"
        criticos += 1
    else:
        situacao = "adequado"
        adequados += 1

    print(f"{produto}: {quantidade} — {situacao}")

print(f"Total de unidades: {total_unidades}")
print(f"Esgotados: {esgotados}")
print(f"Críticos: {criticos}")
print(f"Adequados: {adequados}")

