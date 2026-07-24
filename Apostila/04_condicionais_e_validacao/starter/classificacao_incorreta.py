quantidade = int(input("Quantidade atual: "))
estoque_minimo = 5

if quantidade <= estoque_minimo:
    print("Estoque crítico.")
elif quantidade < 0:
    print("Quantidade inválida.")
elif quantidade == 0:
    print("Estoque esgotado.")
else:
    print("Estoque adequado.")

