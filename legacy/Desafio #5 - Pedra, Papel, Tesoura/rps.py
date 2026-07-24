import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''





rps_moves = [rock, paper, scissors]
print("Bem vindo ao Pedra, Papel e Tesoura - Pythonico \n")
player_move = int(input("Escolha o seu movimento: 0 - Pedra, 1 - Papel, 2 - Tesoura \n"))

if player_move not in [0, 1, 2]:
    print("Movimento inválido... Por favor, escolha 0, 1 ou 2.")
else:
    cpu_move = random.randint(0,2)

    print(f"Você escolheu: {rps_moves[player_move]}")
    print(f"O computador escolheu: {rps_moves[cpu_move]}")

    if (player_move == cpu_move):
        print("Empate!")
    elif (player_move == 0 and cpu_move == 2 or player_move == 1 and cpu_move == 0 or player_move == 2 and cpu_move == 1) :
        print("Você Venceu!!!")
    else:
        print("CPU Venceu!!!")