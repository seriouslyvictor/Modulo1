alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for caracter in original_text:
        if caracter not in alphabet:
            output_text += caracter
            continue

        shifted_position = alphabet.index(caracter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
        print(f"Letra original: {caracter}, quantidade de deslocamento: {shift_amount}, nova letra: {alphabet[shifted_position]}")
    print(f"Aqui está o resultado {encode_or_decode}d: {output_text}")

running = True
while running:
    direction = input("Digite 'encode' para criptografar, digite 'decode' para descriptografar:\n").lower()
    text = input("Digite sua mensagem:\n").lower()
    shift = int(input("Digite o número de deslocamento:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    if input("Digite 'sim' se quiser continuar, ou qualquer outra palavra para sair.").lower() != "sim":
        running = False