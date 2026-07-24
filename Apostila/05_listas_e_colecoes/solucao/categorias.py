categorias = ["Papelaria", "Limpeza", "Alimentos"]
nova_categoria = input("Nova categoria: ")

categorias.append(nova_categoria)
categorias.sort()

print(f"Quantidade: {len(categorias)}")
print(f"Categorias: {categorias}")

