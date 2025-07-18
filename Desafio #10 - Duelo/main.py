# Este exercício é baseado no jogo original do site Higher Lower Game: https://www.higherlowergame.com/
from arts import logo, vs
import random
import json
with open(r"Desafio #10 - Duelo\dados.json", mode="r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)


def formatar_dados(conta):
    nome_conta = conta["termo"]
    descricao_conta = conta["descricao"]
    return f"{nome_conta}, {descricao_conta}"


# def check_answer(user_guess, pesquisa_a, pesquisa_b):
#     if user_guess == "a":
#         if pesquisa_a > pesquisa_b:
#             return True
#         else:
#             return False
#     else:
#         if pesquisa_b > pesquisa_a:
#             return True
#         else:
#             return False
        
def verificar_resposta(palpite_usuario, pesquisa_a, pesquisa_b):
    if pesquisa_a > pesquisa_b:
        return palpite_usuario == "a"
    else:
        return palpite_usuario == "b"



print(logo)
pontos = 0
executando = True

termo_b = random.choice(dados)


while executando:


    termo_a = termo_b
    termo_b = random.choice(dados)

    if termo_a == termo_b:
        termo_b = random.choice(dados)

    print(f"Compare A: {formatar_dados(termo_a)}.")
    print(vs)
    print(f"Contra B: {formatar_dados(termo_b)}.")

    # Pedir palpite do usuário.
    palpite = ""
    while palpite not in ["a", "b"]:
        palpite = input("Qual termo é mais pesquisado? Digite A ou B: ").lower()

    print("\n" * 20)
    print(logo)


    classificacao_a = termo_a["pesquisas"]
    classificacao_b = termo_b["pesquisas"]


    esta_correto = verificar_resposta(palpite, classificacao_a, classificacao_b)

    if esta_correto:
        pontos += 1
        print(f"🎉 Correto! Pontuação: {pontos} 🎉")
    else:
        print(f"💣 Você errou, o jogo acabou. Pontuação Final: {pontos}. 💣")
        executando = False
