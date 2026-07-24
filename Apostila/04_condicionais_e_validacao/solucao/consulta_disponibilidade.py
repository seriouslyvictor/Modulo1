# Valida e classifica a disponibilidade de um produto.
nome_produto = input("Produto: ")
preco = float(input("Preço: "))
quantidade = int(input("Quantidade atual: "))
estoque_minimo = int(input("Estoque mínimo: "))
status = input("Status (ativo ou inativo): ")

if preco <= 0 or quantidade < 0 or estoque_minimo < 0:
    print("Dados inválidos.")
elif status not in ["ativo", "inativo"]:
    print("Status inválido. Digite ativo ou inativo.")
elif status == "inativo":
    print(f"{nome_produto}: produto inativo.")
elif quantidade == 0:
    print(f"{nome_produto}: produto esgotado.")
elif quantidade <= estoque_minimo:
    print(f"{nome_produto}: reposição necessária.")
else:
    print(f"{nome_produto}: estoque adequado.")
