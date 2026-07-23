# Recebe dados textuais e apresenta uma ficha para conferência.
print("=== CADASTRO DE PRODUTO ===")

nome_produto = input("Nome do produto: ")
categoria = input("Categoria: ")
codigo_interno = input("Código interno: ")
localizacao = input("Localização: ")

print()
print("--- FICHA DO PRODUTO ---")
print(f"Produto: {nome_produto}")
print(f"Categoria: {categoria}")
print(f"Código: {codigo_interno}")
print(f"Localização: {localizacao}")

