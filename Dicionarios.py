# Criando um dicionário de Deuses:
deuses_dicionario = {
    'Zeus': "Descrição Zeus",
    "Hades": "Descrição Hades",
    "Poseidon": "Descrição Poseidon"
}

# Resgatando valores do dicionário
print(deuses_dicionario['Zeus'])

# alterando valores de um dicionário
deuses_dicionario["Zeus"] = "O Deus do Raio"
print(deuses_dicionario['Zeus'])

# Adicionando novos valores ao adicinário:
deuses_dicionario["Atena"] =  "A deusa da sabedoria"
print(deuses_dicionario)

# Loopando um dicionário:
# ATENÇÃO: Risco de rasteira ⚠

for deus in deuses_dicionario:
    print(deus) #Somente a chave, não resgatamos os valores assim
    print(deuses_dicionario[deus]) # Aqui resgatamos os valores usando uma chave dinâmica.


# Formas alternativas de acessar todos os valores dos dicionárias :
for nome, descricao in deuses_dicionario.items():
    print(f"{nome}: {descricao}")

# Apenas as chaves:
print(deuses_dicionario.keys())

# Apenas os valores:
print(deuses_dicionario.values())


# Regastando valores "sem erros":
# print(deuses_dicionario['Apollo']) # Gera um Key Error, não há essa chave no nosso dicionário
print(deuses_dicionario.get("Apollo", "Deus não encontrado!")) # Não gera um erro de fato, apenas informa que o Deus não existe

# Apagando um único valor de um dicionário:
del deuses_dicionario['Poseidon']
print(deuses_dicionario)

# Limpando o dicionário inteiro:
deuses_dicionario = {}

deuses_info = {
    "Zeus": {"dominio": "céu", "arma": "raios"},
    "Hades": {"dominio": "submundo", "arma": "elmo da invisibilidade"}
}

print(deuses_info["Hades"]["arma"])

# Mini Exercicio 1
# Crie um programa que irá converter uma pontuação de almas em uma avaliação de almas.
# Exemplo: 
# entrada "Brizola": 40
# saida: "Brizola": "Neutra"
# A saída deve ser um novo dicionário contendo os nomes original e a avaliação.

# As pontuação devem seguir os critérios abaixo:
# 81 ~ 100: Justa
# 61 ~ 80: Boa
# 41 ~ 60: Neutra
# 21 ~ 40: Ruim
# 0 ~ 20: Injusta

pontuacao_almas = {
    'Brizola': 40,
    'Collor': 10,
    'Ada Lovelace': 85,
    'Verso': 100,
    'Odesnildo': 90,
    'Melania': 55
}

avaliacao_almas = {}

