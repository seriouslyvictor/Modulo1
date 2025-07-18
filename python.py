tem_dinheiro = True
esta_chovendo = False
tem_guarda_chuva = False

if tem_dinheiro and (esta_chovendo or tem_guarda_chuva):
    print("Pode sair de casa!")
else:
    print("Fica em casa.")

tem_fome = True
tem_comida = True
fogao_funcionando = False

if tem_fome and tem_comida and fogao_funcionando:
    print("Vai cozinhar!")
else:
    print("Não vai cozinhar.")

nota = 4
faltas = 2

if nota >= 7 or faltas <= 1:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")

logado = False

if not logado:
    print("Acesso negado. Faça login.")
else:
    print("Bem-vindo de volta!")


senha = "tiburcioIV"

if len(senha) > 6:
    print("Senha forte.")
else:
    print("Senha fraca.")



sayajin = ["Goku", "Vegeta", "Gohan"]

if "Freeza" in sayajin:
    print("Freeza é um sayajin!")
else:
    print("Freeza não é um sayajin....")


import random
d20 = random.randint(0,20)

if d20 == 20:
    print("Acerto Crítico!")
elif d20 == 0:
    print("Erro Crítico!")
else:
    print(f"Você rolou {d20}")


profissões = ["Programador", "Engenheiro", "Médico", "Professor"]
idade = 38
cargo = "Programador"

if cargo in profissões and idade >= 30:
    print("O psiquiatra irá te atender.")
else:
    print("Sua saúde mental está em dia.")



hora_atual = 14

if (hora_atual >= 8 and hora_atual <= 12) or (hora_atual >= 13 and hora_atual <= 18):
    print("Estamos abertos!")
else:
    print("Estamos fechados.")


pokemons = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Pikachan", "Zapdos"]

novo_pokemon = "DIGLET"
if len(pokemons) >= 6:
    print("Você já tem 6 pokémons, não pode capturar mais!")
else:
    pokemons.append(novo_pokemon)
    print(f"Você capturou {novo_pokemon}!")

alma = "justa"
redimidas = 0   
corrompidas = 0

if alma == "justa":
    redimidas += 1
elif alma == "corrompida":
    corrompidas += 1


resultado = []
for i in range(3):
    resultado.append(i * 2)
print(resultado)




for numero in range(5):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")

sorteio = 0
tentativas = 0
import random
while sorteio != 777:
    sorteio = random.randint(111, 999)
    tentativas += 1
print(f"🎉 Conseguimos o 777 em {tentativas} tentativas.")



nums = [2, 4, 6, 8]
total = 0
for num in nums:
    total += num


letras = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"  
simbolos = "!@#$%^&*()_+"
import random
senha= []

nr_letras = 4
nr_numeros = 2
nr_simbolos = 1

for i in range(nr_letras):
    senha.append(random.choice(letras))
for i in range(nr_numeros):
    senha.append(random.choice(numeros))
for i in range(nr_simbolos):
    senha.append(random.choice(simbolos))




for i in range(10):
    senha.append(random.choice(simbolos))




i = 0
while i >= 0:
    senha.append(random.choice(numeros))
    i += 1



senha = ["a", "b", "c"]
while senha:
    char = senha.pop()
    print(char)


