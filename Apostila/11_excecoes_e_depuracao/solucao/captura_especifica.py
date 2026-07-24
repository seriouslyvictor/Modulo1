try:
    preco = float(input("Preço: "))
    quantidade = 4
    total = preco * quantidade
    print(f"Total: R$ {total:.2f}")
except ValueError:
    print("Digite um preço numérico.")
