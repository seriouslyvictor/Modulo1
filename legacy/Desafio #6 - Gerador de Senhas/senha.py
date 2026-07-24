import random

#TODO 1
#Crie 3 listas separadas contendo: letras, números e simbolos.

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["!", "@", "#", "$", "%", "^", "&", "*"]

#TODO 2
# Exibir a tela de boas vindas ao gerador de senhas.
# Perguntar quantas letras, números e símbolos serão usados na senha, guarde os valores em variáveis apropriadas.

print("Bem-vindo ao gerador de senhas!")
print("Você pode escolher o tamanho da senha e os tipos de caracteres que deseja incluir.")

nr_letras = int(input("Quantas letras você quer na senha? "))
nr_numeros = int(input("Quantos números você quer na senha? "))
nr_simbolos = int(input("Quantos símbolos você quer na senha? "))


#TODO 3
# Crie uma lista VAZIA chamada "senha" que irá conter os caracteres da senha
# Faça um loop que irá sortear aleatoriamente uma das letras na lista de letras, o loop deve ser executado pelo número de vezes que foi informado pelo usuário, dentro do loop, faça o append() desse caractere na lista "senha".
# DICA: O número de letras já deve estar armazenado em uma variável!

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

#TODO 4
#Embaralhe a lista "senha", lembre-se do método shuffle.
random.shuffle(senha)

#TODO 5
# Converta a lista senha em uma string(texto), pesquise no Google/LLM como isso pode ser feito.
# Exiba a senha para o usuário!
senha = "".join(senha) # Converte a lista em uma string
print(f"Sua senha gerada é: {senha}")
print("Lembre-se de guardar sua senha em um local seguro!")
print("Obrigado por usar o gerador de senhas!")

#TODO 6
# Comemore! Seu programa está pronto 🙌
