#  DESAFIO #4 - PIZZA-O-TRON MASTER 9000 🍕🤖  
#  Você foi contratado como programador oficial da rede intergaláctica de pizzarias Pizza-o-Tron!  
#  Sua missão é desenvolver um sistema automatizado para calcular o valor do pedido de pizza de um cliente.  
#  Para isso, o sistema deve seguir as seguintes regras:  
#  1️⃣ Perguntar o tamanho da pizza (S = Pequena, M = Média, L = Grande)  
#     - Pequena custa R$20  
#     - Média custa R$30  
#     - Grande custa R$45  
#     - Se o cliente digitar algo inválido, considerar Pequena (R$15) como padrão  
#  2️⃣ Perguntar se o cliente deseja MAIS QUEIJO por +R$5  
#  3️⃣ Perguntar se o cliente deseja BORDA RECHEADA por +R$7  
#  No final, o programa deve somar tudo e exibir o valor total do pedido.  











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
