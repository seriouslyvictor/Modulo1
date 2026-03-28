import random, arts
import time

def sortear_cartas():
    baralho = [11,2,3,4,5,6,7,8,9,10,10,10]
    carta_baralho = random.choice(baralho)
    return carta_baralho

def calcular_pontos(hand):
    if sum(hand) == 21 and len(hand) == 2:
        # Indicação do blackjack / 21
        return 0

    #lógica para trocar o valor do ás conforme o número de cartas
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    
    return sum(hand)

def checar_vitoria(p1,p2):
    if p1 > 21:
        print("O jogador estourou a mão, vitória do CPU!")
    elif p1 == 0:
        print("O jogador venceu com um blackjack!")
    elif p1 > p2:
        print("O jogador venceu por pontos!")
    elif p2 > 21:
        print("O CPU estourou a mão!")
    elif p2 == 0:
        print("CPU venceu com um blackjack!")
    elif p2 > p1:
        print("O CPU venceu por pontos")
    else:
        print("Empate!")
    

def iniciar_jogo():
    print(arts.logo)
    time.sleep(0.5)
    print("Bem vindo ao 21 🎴")
    print("Lembre-se: A casa sempre ganha!")
    
    cartas_jogador = []
    cartas_cpu =[]
    pontos_jogador = -1
    pontos_cpu = -1
    jogo_rolando = True

    for _ in range(0,2):
        cartas_jogador.append(sortear_cartas())
        cartas_cpu.append(sortear_cartas())
    
    while jogo_rolando:
        pontos_jogador = calcular_pontos(cartas_jogador)
        pontos_cpu = calcular_pontos(cartas_cpu)

        print(f"Suas cartas são {cartas_jogador}, você tem {pontos_jogador} pontos.")
        time.sleep(0.5)
        print(f"O CPU possui {len(cartas_cpu)} cartas, a primeira carta é: {cartas_cpu[0]}")

        # Checando se há vitórias ou mãos estouradas
        if pontos_jogador == 0 or pontos_cpu == 0 or pontos_jogador > 21:
            jogo_rolando = False
        else:
            comprar_carta = input("Quer comprar mais cartas? Digite S ou N \n").lower()
            if comprar_carta == "s":
                cartas_jogador.append(sortear_cartas())
            else:
                jogo_rolando = False
        
    while pontos_cpu <= 17 and pontos_cpu != 0 and pontos_jogador <= 21:
        cartas_cpu.append(sortear_cartas())
        # Atualizar os pontos para não entrar em loop infinito!!
        pontos_cpu = calcular_pontos(cartas_cpu)
        # Jogo será encerrado, preparando condições:
    
    print("/--------------------/")
    print(f"Suas cartas: {cartas_jogador}\nPontuação: {pontos_jogador}")
    time.sleep(0.5)
    print(f"CPU hand's {cartas_cpu}\nPontuação: {pontos_cpu}")
    time.sleep(0.5)
    print("/--------------------/")
    time.sleep(0.5)
    checar_vitoria(pontos_jogador, pontos_cpu)

while input("Aceita uma partida de 21? S ou N\n").lower() == "s":
    print("\n" *20)
    iniciar_jogo()