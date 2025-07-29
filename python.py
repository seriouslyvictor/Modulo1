# tem_dinheiro = True
# esta_chovendo = False
# tem_guarda_chuva = False

# if tem_dinheiro and (esta_chovendo or tem_guarda_chuva):
#     print("Pode sair de casa!")
# else:
#     print("Fica em casa.")

# tem_fome = True
# tem_comida = True
# fogao_funcionando = False

# if tem_fome and tem_comida and fogao_funcionando:
#     print("Vai cozinhar!")
# else:
#     print("Não vai cozinhar.")

# nota = 4
# faltas = 2

# if nota >= 7 or faltas <= 1:
#     print("Aluno aprovado!")
# else:
#     print("Aluno reprovado.")

# logado = False

# if not logado:
#     print("Acesso negado. Faça login.")
# else:
#     print("Bem-vindo de volta!")


# senha = "tiburcioIV"

# if len(senha) > 6:
#     print("Senha forte.")
# else:
#     print("Senha fraca.")



# sayajin = ["Goku", "Vegeta", "Gohan"]

# if "Freeza" in sayajin:
#     print("Freeza é um sayajin!")
# else:
#     print("Freeza não é um sayajin....")


# import random
# d20 = random.randint(0,20)

# if d20 == 20:
#     print("Acerto Crítico!")
# elif d20 == 0:
#     print("Erro Crítico!")
# else:
#     print(f"Você rolou {d20}")


# profissões = ["Programador", "Engenheiro", "Médico", "Professor"]
# idade = 38
# cargo = "Programador"

# if cargo in profissões and idade >= 30:
#     print("O psiquiatra irá te atender.")
# else:
#     print("Sua saúde mental está em dia.")



# hora_atual = 14

# if (hora_atual >= 8 and hora_atual <= 12) or (hora_atual >= 13 and hora_atual <= 18):
#     print("Estamos abertos!")
# else:
#     print("Estamos fechados.")


# pokemons = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Pikachan", "Zapdos"]

# novo_pokemon = "DIGLET"
# if len(pokemons) >= 6:
#     print("Você já tem 6 pokémons, não pode capturar mais!")
# else:
#     pokemons.append(novo_pokemon)
#     print(f"Você capturou {novo_pokemon}!")

# alma = "justa"
# redimidas = 0   
# corrompidas = 0

# if alma == "justa":
#     redimidas += 1
# elif alma == "corrompida":
#     corrompidas += 1


# resultado = []
# for i in range(3):
#     resultado.append(i * 2)
# print(resultado)




# for numero in range(5):
#     if numero % 2 == 0:
#         print(f"{numero} é par")
#     else:
#         print(f"{numero} é ímpar")

# sorteio = 0
# tentativas = 0
# import random
# while sorteio != 777:
#     sorteio = random.randint(111, 999)
#     tentativas += 1
# print(f"🎉 Conseguimos o 777 em {tentativas} tentativas.")



# nums = [2, 4, 6, 8]
# total = 0
# for num in nums:
#     total += num


# letras = "abcdefghijklmnopqrstuvwxyz"
# numeros = "0123456789"  
# simbolos = "!@#$%^&*()_+"
# import random
# senha= []

# nr_letras = 4
# nr_numeros = 2
# nr_simbolos = 1

# for i in range(nr_letras):
#     senha.append(random.choice(letras))
# for i in range(nr_numeros):
#     senha.append(random.choice(numeros))
# for i in range(nr_simbolos):
#     senha.append(random.choice(simbolos))




# for i in range(10):
#     senha.append(random.choice(simbolos))




# i = 0
# while i >= 0:
#     senha.append(random.choice(numeros))
#     i += 1



# senha = ["a", "b", "c"]
# while senha:
#     char = senha.pop()
#     print(char)


# def contar(palavra):
#     vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
#     for letra in palavra.lower():
#         if letra in palavra:
#             vogais["letra"] += 1
#         else:
#     return sum(vogais.values())

# print(contar("Python"))

def contar_vogais(palavra):
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in palavra.lower():
        if letra in vogais:
            vogais[letra] += 1
    print(vogais)
    return sum(vogais.values())

print(contar_vogais("Python"))


def atualizar_notas(estudantes, nome, nota):
    if nome in estudantes:
        estudantes[nome].append(nota)
    else:
        estudantes[nome] = [nota]
    return estudantes

notas = {'Patrick': [85]}
atualizar_notas(notas, 'Bob Esponja', 90)
print(notas)

def filtrar_dicionario(dados, valor_minimo):
    resultado = {}
    for chave, valor in dados.items():
        if valor >= valor_minimo:
            resultado[chave] = valor
    return resultado

pontuacoes = {'redes_computadores': 85, 
              'programacao_internet': 92, 
              'engenharia_software': 78}
print(len(filtrar_dicionario(pontuacoes, 80)))

def processar_dados(numeros):
    resultado = {'pares': [], 'impares': []}
    for num in numeros:
        if num % 2 == 0:
            resultado['pares'].append(num)
        else:
            resultado['impares'].append(num)
    return resultado

dados = processar_dados([1, 2, 3, 4, 5])
print(dados['pares'])





def encontrar_valor_maximo(dicionario):
    valor_max = 0
    for valor in dicionario.values():
        print(type(valor))
        if isinstance(valor, (int, float)) and valor > valor_max:
            valor_max = valor
    return valor_max
valores= {'a': 10, 'b': 5, 'c': 15, 'd': "20"}
print(encontrar_valor_maximo(valores))

def mesclar_dicionarios(dict1, dict2):
    # Cria uma cópia do primeiro dicionário
    resultado = dict1.copy() 
    for chave, valor in dict2.items():
        if chave in resultado:
            resultado[chave] += valor
        else:
            resultado[chave] = valor
    return resultado

a = {'x': 5, 'y': 10}
b = {'x': 3, 'z': 8}
c = mesclar_dicionarios(a, b)
print(c['x'])


def agrupar_por_tamanho(palavras):
    grupos = {}
    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho not in grupos:
            grupos[tamanho] = []
        grupos[tamanho].append(palavra)
    return grupos

palavras = ["gato", "cao", "elefante", "rato"]
resultado = agrupar_por_tamanho(palavras)
print(resultado[3])

def encontrar_chaves_comuns(dict1, dict2):
    comuns = []
    for chave in dict1:
        if chave in dict2:
            comuns.append(chave)
    return comuns

a = {'x': 1, 'y': 2, 'z': 3}
b = {'y': 5, 'z': 6, 'w': 7}
print(encontrar_chaves_comuns(a, b))

personagem = {'nome': 'Kratos', 
              'idade': 30}
resultado = personagem['nome']
print(resultado)

cores = {'azul': '#0000FF', 
         'verde': '#00FF00', 
         'vermelho': '#FF0000'}
print(len(cores))

aluno = {'nome': 'Mariana', 
         'curso': 'Engenharia'}

print('idade' in aluno)


def validar_dados(dicionario, chaves_obrigatorias):
    faltando = []
    for chave in chaves_obrigatorias:
        if chave not in dicionario or dicionario[chave] is None:
            faltando.append(chave)
    return faltando

dados_usuario = {'nome': 'Atreus', 'idade': 15, 'email': None}
obrigatorias = ['nome', 'idade', 'email']
print(validar_dados(dados_usuario, obrigatorias))

def atualizar_estoque(estoque, transacoes):
    for item, alteracao in transacoes.items():
        if item in estoque:
            estoque[item] += alteracao
            if estoque[item] < 0:
                estoque[item] = 0
        else:
            estoque[item] = alteracao
            if estoque[item] < 0:
                estoque[item] = 0
    return estoque

estoque = {'macas': 10, 'bananas': 5}
mudancas = {'macas': -15, 'laranjas': 8, 'bananas': 3}
resultado = atualizar_estoque(estoque, mudancas)
print(resultado['macas'])

import json
# with open("dados.json", "r", encoding="utf-8") as f:
#     conteudo = json.load(f)

dicionario = {"nome": "Thor", 
              "idade": 1500, 
              "poderes": ["raio", "força"]} 
with open("thor.json", "w", encoding="utf-8") as f:
    json.dump(dicionario, f, ensure_ascii=False, indent=4)
