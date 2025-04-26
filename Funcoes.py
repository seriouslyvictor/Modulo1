# Vamos aprender funções!
# Funções são blocos de código reutilizáveis que são executadas SOMENTE quando 'invocadas' pelo seu nome.
# Veja o exemplo abaixo:

def saudacao():
    print("Olá, Tibúrcio!")

# Note que o () é necessário para invocar a função.
saudacao()


# As funções também podem receber parâmetros, ou seja, informações para que elas funcionem como esperado:
def saudacao_param(nome):
    print(f"Olá, {nome}")

saudacao_param("Maria") 

# Funções podem ter um "retorno", uma única informação que é produzida ao final da execução da função:
# Na função abaixo, caso não houvesse o 'return', a operação de duplicação seria inútil, pois não teriamos como resgatar esse valor.
def duplicar(num):
    return num * 2

resultado = duplicar(4)
print(resultado) 

# Funções podem, logicamente, executar qualquer instrução que você já aprendeu até aqui, vamos para alguns exemplos:
def grito(palavra):
    print(palavra.upper() + "!")

grito("olá")

import random

def profecia_apollo():
    profecias = ["Você encontrará um tesouro escondido", "Um grande amor está a caminho", "Cuidado com os inimigos"]
    return random.choice(profecias)

def tiro_artemis(animal):
    if animal == "cervo":
        print("O cervo é um animal sagrado para Ártemis.")
    else:
        print(f"Artemis atinge o {animal} com mira perfeita!.")

def julgamento_hades(pontuacao):
    if pontuacao >= 80:
        print("Hades envia a alma para o Elísio.")
    elif pontuacao >= 50:
        print("Hades envia a alma para o Limbo .")
    else:
        print("Hades envia a alma para o Tártaro, sofrimento eterno.")

    