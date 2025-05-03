from arts import logo, vs
import random
import json
with open(r"Desafio #10 - Duelo\dados.json", mode="r", encoding="utf-8") as arquivo:
    data = json.load(arquivo)


def format_data(account):
    account_name = account["term"]
    account_descr = account["description"]
    return f"{account_name}, {account_descr}"


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
        
def check_answer(user_guess, pesquisa_a, pesquisa_b):
    if pesquisa_a > pesquisa_b:
        return user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
pontos = 0
executando = True

termo_b = random.choice(data)


while executando:


    termo_a = termo_b
    termo_b = random.choice(data)

    if termo_a == termo_b:
        termo_b = random.choice(data)

    print(f"Compare A: {format_data(termo_a)}.")
    print(vs)
    print(f"Contra B: {format_data(termo_b)}.")

    # Ask user for a guess.
    guess = ""
    while guess not in ["a", "b"]:
        guess = input("Qual termo é mais pesquisado? Digite A ou B: ").lower()

    print("\n" * 20)
    print(logo)


    rank_a = termo_a["searches"]
    rank_b = termo_b["searches"]


    is_correct = check_answer(guess, rank_a, rank_b)

    if is_correct:
        pontos += 1
        print(f"🎉 Correto! Pontuação: {pontos} 🎉")
    else:
        print(f"💣 Você errou, o jogo acabou. Pontuação Final: {pontos}. 💣")
        executando = False
