# Recebe os dados textuais de um produto e apresenta um comprovante.
print("=== NOVO PRODUTO ===")

nome_produto = input("Nome: ")
marca = input("Marca: ")
categoria = input("Categoria: ")
codigo_interno = input("Código interno: ")
localizacao = input("Localização: ")

print()
print("=== COMPROVANTE ===")
print(f"Produto: {nome_produto}")
print(f"Marca: {marca}")
print(f"Categoria: {categoria}")
print(f"Código: {codigo_interno}")
print(f"Localização: {localizacao}")
print("Cadastro textual concluído.")

