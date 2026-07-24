# Verifica se o preço informado é maior que zero.
nome_produto = input("Produto: ")
preco = float(input("Preço: "))

if preco > 0:
    print(f"{nome_produto}: preço válido.")
else:
    print(f"{nome_produto}: preço inválido.")

