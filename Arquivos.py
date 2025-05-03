
# Abrindo um arquivo para leitura.

with open("test.txt", encoding='utf-8') as file:
    conteudo = file.read()
    print(conteudo)

# Escrevendo informações no arquivo.
# ⚠ Isso irá apagar todo conteúdo prévio!!
with open("test.txt", encoding='utf-8', mode="w") as file:
    file.write("Hello, is this dog?")

# AVISO: Maneira "old school", relativamente complexa para ler e resgatar informações de arquivos simples.
deuses_dicionario = {
    'Zeus': "Descrição Zeus",
    "Hades": "Descrição Hades",
    "Poseidon": "Descrição Poseidon"
}

with open("test.txt", encoding='utf-8', mode="a") as file:
    for deus, desc in deuses_dicionario.items():
        file.write(f"\n{deus}: {desc}")


dicto = {}
with open("test.txt", mode="r", encoding="UTF-8") as arquivo:
    dados = arquivo.readlines()
    print(dados)
    for linha in dados:
        linha = linha.strip()
        if ":" in linha:
            chave, valor = linha.split(":", 1)
            print(chave, valor)
            dicto[chave.strip()] = valor.strip()
print(dicto)

# Maneira moderna, usando arquivos JSON(JavaScript Object Notation)
import json

with open("deuses.json", mode="w", encoding="UTF-8") as arquivo:
    json.dump(deuses_dicionario, arquivo, ensure_ascii=False)

with open("deuses.json", mode="r", encoding="UTF-8") as arquivo:
    new_dicto = json.load(arquivo)
    print(new_dicto)
    print(new_dicto["Zeus"])

#Mini Desafio #1
# Altere o programa do Desafio #9 para os seguintes critérios:
# 1. Carregar a lista dos Deuses a partir de um JSON em um dicionário chamado livro_dos_deuses
# 2. Acresce uma nova opção chamada: 5. Salvar e sair, essa opção deve salvar o dicionário livro_dos_deuses no arquivo JSON lido anteriormente, use o modo "w" para isso.
# 3.