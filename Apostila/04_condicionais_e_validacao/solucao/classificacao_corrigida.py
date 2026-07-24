quantidade = int(input("Quantidade atual: "))
estoque_minimo = 5

if quantidade < 0:
    print("Quantidade inválida.")
elif quantidade == 0:
    print("Estoque esgotado.")
elif quantidade <= estoque_minimo:
    print("Estoque crítico.")
else:
    print("Estoque adequado.")

