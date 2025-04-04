print("Bem-vindo ao Pizza-o-Tron MASTER 9000 🍕")
print("Vamos montar seu pedido:")

# Escolha do tamanho
size = input("Qual o tamanho da pizza? (S = Pequena, M = Média, L = Grande): ").upper()

# Adicional de pepperoni
add_pepperoni = input("Deseja adicionar mais queijo por +R$5? (S/N): ").upper()

# Borda recheada
stuffed_crust = input("Deseja borda recheada por +R$7? (S/N): ").upper()

# Preço base
bill = 0

if size == "S":
    bill = 20
elif size == "M":
    bill = 30
elif size == "L":
    bill = 45
else:
    print("Tamanho inválido. Usaremos pizza Pequena por padrão.")
    bill = 15

# Adicionais
if add_pepperoni == "S":
    bill += 5

if stuffed_crust == "S":
    bill += 7

print(f"Seu pedido ficou em R${bill},00. Obrigado por escolher Pizza-o-Tron MASTER 9000 🍕🧀")
