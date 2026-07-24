import random

from arte import splash, forca
from palavras import lista_palavras

erros = 0

print(splash)

chosen_word = random.choice(lista_palavras)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Palavra: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{erros}/6 ERROS RESTANTES****************************")
    guess = input("Chute uma letra: ").lower()

    if guess in correct_letters:
        print(f"Você já tentou essa letra {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        erros += 1
        print(f"Você chutou {guess}, essa letra não está na palavra. A forca aperta.....")

        if erros > 6:
            game_over = True

            print(f"A palavra era {chosen_word}. Você perdeu!")

    if "_" not in display:
        game_over = True
        print("Dessa vez, escapou da forca!")

    try:
        print(forca[erros])
    except IndexError:
        print("/==== Game Over! ====/")