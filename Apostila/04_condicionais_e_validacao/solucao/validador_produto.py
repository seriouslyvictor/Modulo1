# Valida dados numéricos e classifica o nível do estoque.
nome_produto = input("Produto: ")
preco = float(input("Preço: "))
quantidade = int(input("Quantidade atual: "))
estoque_minimo = int(input("Estoque mínimo: "))

if preco <= 0 or quantidade < 0 or estoque_minimo < 0:
    print("Cadastro inválido.")
elif quantidade == 0:
    print(f"{nome_produto}: estoque esgotado.")
elif quantidade <= estoque_minimo:
    print(f"{nome_produto}: estoque crítico.")
else:
    print(f"{nome_produto}: estoque adequado.")

