#  Desafio #1 -- Seu nome Ninja! 
#  Você foi transportado para o universo do NARUTO e agora terá que adotar um nome ninja para ser reconhecido. 
#  Sua tarefa é construir um gerador de nome ninja com base em 3 perguntas: 
#  1 - Qual o seu Nome? 
#  2 - Em que cidade você nasceu? 
#  3 - Qual seu animal preferido?  

# O resultado deverá ser um alert() ou console.log() no seguinte modelo:  Você será conhecido como "seu nome" da vila oculta de "cidade", invocador de "animal preferido".















print("Desafio #1 -- Seu Nome Ninja!")
print("Você foi transportado para o universo do NARUTO e agora terá que adotar um nome ninja para ser reconhecido.")
print("Sua tarefa é construir um gerador de nome ninja com base em 3 perguntas:")
print("1 - Qual o seu Nome?")
print("2 - Em que cidade você nasceu?")
print("3 - Qual seu animal preferido?\n")
nome = input("Qual o seu Nome? ")
cidade = input("Em que cidade você nasceu? ")
animal = input("Qual seu animal preferido? ")

nome_ninja = f'Você será conhecido como {nome} da Vila Oculta de {cidade}, invocador de {animal}.'
print(nome_ninja)