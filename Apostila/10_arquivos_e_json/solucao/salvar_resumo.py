nome = input("Nome: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preço: "))

with open("resumo.txt", mode="w", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Quantidade: {quantidade}\n")
    arquivo.write(f"Preço: R$ {preco:.2f}\n")

with open("resumo.txt", mode="r", encoding="utf-8") as arquivo:
    print(arquivo.read())

