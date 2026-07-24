produtos = ["Caderno", "Caneta", "Borracha", "Lápis"]
quantidades = [10, 0, 3, 5]
estoque_minimo = 3

total_unidades = 0
produtos_esgotados = 0
produtos_criticos = 0

for indice in range(len(produtos)):
    print(f"{produtos[indice]}: {quantidades[indice]}")
    total_unidades += quantidades[indice]

    if quantidades[indice] == 0:
        produtos_esgotados += 1
    elif quantidades[indice] <= estoque_minimo:
        produtos_criticos += 1

print(f"Total de unidades: {total_unidades}")
print(f"Produtos esgotados: {produtos_esgotados}")
print(f"Produtos críticos: {produtos_criticos}")

