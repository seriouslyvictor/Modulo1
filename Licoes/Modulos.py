# Importando um módulo
# Módulo é um arquivo que contém funções e variáveis que podem ser reutilizadas em outros arquivos
import random

# ---------------------------
# 1. random.randint(a, b)
# ---------------------------
# Um número inteiro aleatório entre a e b (inclusive)

print("Número aleatório entre 1 e 10:", random.randint(1, 10))


# ---------------------------
# 2. random.choice(list)
# ---------------------------
# Seleciona um item aleatório de uma lista
# Exemplo: escolher uma cor aleatória de uma lista de cores

colors = ["vermelho", "azul", "verde", "amarelo"]
chosen_color = random.choice(colors)
print("Cor aleatória:", chosen_color)


# ---------------------------
# 3. random.random()
# ---------------------------
# Um número de ponto flutuante aleatório entre 0.0 e 1.0, não incluindo 1.0

print("Aleatório entre 0 e 1:", random.random())


# ---------------------------
# 4. random.shuffle(list)
# ---------------------------
# Embalhar uma lista de itens, mudando a ordem deles aleatoriamente
# Exemplo: embaralhar uma lista de cartas

cards = ["Ás", "Rei", "Rainha", "Valete", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
print("Antes do 'shuffle':", cards)
random.shuffle(cards)
print("Após o 'shuffle':", cards)


# ---------------------------
# 5. Gerar um escolha aleatória para um jogo de Pedra, Papel e Tesoura
# ---------------------------
choices = ["pedra", "papel", "tesoura"]
computer_choice = random.choice(choices)
print("Computador escolheu:", computer_choice)


# Exemplos com condicionais
# ---------------------------
# Example 1: Rolando um d6
# ---------------------------
dice_roll = random.randint(1, 6)
print("Você tirou:", dice_roll)

if dice_roll == 6:
    print("🎉 tirou o número mais alto!")
elif dice_roll == 1:
    print("😢 Rolou baixo....")
else:
    print("Normal!")

# ---------------------------
# Example 2: Simulador de clima
# ---------------------------
weather = random.choice(["ensolarado", "chuvoso", "nublado", "tempestade"])
print("O clima de hoje é:", weather)

if weather == "ensolarado":
    print("Leve seu óculos de sol! 😎")
elif weather == "chuvoso":
    print("Um guarda-chuva será útil. ☔")
elif weather == "tempestade":
    print("Se possível, fique em casa. ⛈️")
else:
    print("Típico céu paulista! ☁️")

# ---------------------------
# Example 3: Magic 8-ball
# ---------------------------
question = input("Digite sua pergunta: \n")
print(f"Você perguntou: {question}")

answers = [
    "Sim, com certeza.",
    "Não tenho certeza.",
    "Jamais!",
    "Hmm... díficil dizer.",
    "Provavelmente sim!",
    "Provavelmente não.",
]

response = random.choice(answers)
print("🎱 Magic 8-ball responde:", response)
