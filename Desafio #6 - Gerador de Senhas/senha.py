import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["!", "@", "#", "$", "%", "^", "&", "*"]


print("Bem-vindo ao gerador de senhas!")
print("Você pode escolher o tamanho da senha e os tipos de caracteres que deseja incluir.")

nr_letras = int(input("Quantas letras você quer na senha? "))
nr_numeros = int(input("Quantos números você quer na senha? "))
nr_simbolos = int(input("Quantos símbolos você quer na senha? "))

tamanho_senha = nr_letras + nr_numeros + nr_simbolos
print(f"O tamanho total da senha será: {tamanho_senha} caracteres.")
print("Gerando sua senha...")
senha = []
for letra in range(nr_letras):
    senha.append(random.choice(letras))
for numero in range(nr_numeros):
    senha.append(random.choice(numeros))
for simbolo in range(nr_simbolos):
    senha.append(random.choice(simbolos))

random.shuffle(senha)
senha = "".join(senha) # Converte a lista em uma string
print(f"Sua senha gerada é: {senha}")
print("Lembre-se de guardar sua senha em um local seguro!")
print("Obrigado por usar o gerador de senhas!")


