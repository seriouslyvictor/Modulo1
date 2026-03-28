# --------------------------------
# 1. FOR LOOP
# --------------------------------

print("Vamos fazer nossas reps na academia:")
for index in range(11):  
    print("🏋️‍♀️ rep número: ", index)


# --------------------------------
# 2. FOR LOOP
# --------------------------------

deuses = ["Apollo", "Zeus", "Hades"]
print("\nVamos imprimir todos os Deuses da lista:")

for deus in deuses:
    print(f"{deus} é um Deus!") 


# --------------------------------
# 3. WHILE LOOP
# --------------------------------

print("\nForçando um loop com WHILE:")

opcao = ""
while opcao != "sair":
    opcao = input("Digite 'Sair' para sair do loop: ").lower()


# --------------------------------
# 4. WHILE LOOP
# --------------------------------

print("\nVamos rolar o dado até que saia um 6...")

import random
dado = 0
tentativas = 0

while dado != 6:
    dado = random.randint(1, 6)
    print("Jogando o dado...", dado)
    tentativas += 1
    
print(f"🎉 Conseguimos o 6 em {tentativas} tentativas.")


# --------------------------------
# 5. Loop com IF
# --------------------------------

print("\nImprimindo números pares ou ímpares de 1 até 10:")

for num in range(11):
    if num % 2 == 0:
        print(num, "é par")
    else:
        print(num, "é ímpar")

# --------------------------------
# 6. Descobrindo se algo existe em uma lista ou "frase"
# --------------------------------

deuses = ["Apollo", "Zeus", "Hades"]
pergunta = input("Digite o nome de um Deus Grego: \n")
if pergunta in deuses:
    print(f"Correto {pergunta} é um Deus Grego!")
else:
    print(f"{pergunta} não é um Deus Grego...")

email = input("Digite seu email: \n")
if "@" in email:
    print("Obrigado!")
else:
    print("Este não parece ser um email válido...")

# --------------------------------
# Mini Desafios
# --------------------------------

# 1. Crie um loop que irá somar todos os números de 1 a 100 e imprimir o resultado.
soma = 0
for i in range(1, 101):
    soma += i
print(f"\nA soma de 1 a 100 é: {soma}")

# 2. Pergunte um número para o usuário e imprima a tabuadasa desse número de 1 a 10.
numero = int(input("\nDigite um número para ver sua tabuada: "))
print(f"\nTabuada do {numero}:")
for num in range(11):
    print(f"{numero} x {num} = {numero * num}")

# 3. Sorteie um número entre 111 e 999 até que a combinação seja 777, imprimir o número de tentativas para conseguir o 777.
sorteio = 0
tentativas = 0
while sorteio != 777:
    sorteio = random.randint(111, 999)
    tentativas += 1
print(f"🎉 Conseguimos o 777 em {tentativas} tentativas.")

# 4. Faça um loop que retona o fatorial de um número.
# O fatorial de um número n é a multiplicação de todos os números inteiros de 1 até N.
# Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
fatorial = 1
numero = int(input("\nDigite um número para calcular o fatorial: "))
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero} é: {fatorial}")  

#5 . Faça um loop que onde Hades irá percorrer uma lista de almas e condenar ou salvar cada uma delas, ao final do loop, imprima quantas almas foram salvas e quantas foram condenadas.

almas = ["justa", "injusta", "neutra", "justa", "injusta", "neutra", "justa", "injusta", "neutra", "justa", "injusta", "injusta", "injusta", "justa", "injusta", "neutra"]
condenadas = 0
redimidas = 0

for alma in almas:
    if alma == "justa":
        redimidas += 1
    elif alma == "injusta":
        condenadas += 1
    else:
        print("Hades não toma nenhuma ação.")
print(f"\nAlmas redimidas: {redimidas}")
print(f"Almas condenadas: {condenadas}")

# Desafio 6 - Gerador de Senhas.
# Desafio 7 - Jogo da Forca.