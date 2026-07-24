from art import splash
import json
# Livro sagrado com alguns deuses já inseridos

with open ("Desafio #9 - Enciclopedia dos Deuses Turbo/deuses.json", mode="r", encoding="UTF-8") as arquivo:
    livro_dos_deuses = json.load(arquivo)
print(livro_dos_deuses)

# Loop principal do programa
print(splash)
executando = True
while executando:
    print("\n-- O Livro dos Deuses --")
    print("1. Consultar um deus")
    print("2. Adicionar um novo deus")
    print("3. Atualizar um deus existente")
    print("4. Listar todos os deuses")
    print("5. Salvar e sair")
    print("6. Sair sem salvar")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do deus: ")
        if nome in livro_dos_deuses:
            print(f"{nome}: {livro_dos_deuses[nome]}")
        else:
            print("Este deus não está no livro.")

    elif escolha == "2":
        nome = input("Nome do novo deus: ")
        if nome in livro_dos_deuses:
            print("Este deus já está registrado.")
        else:
            descricao = input("Descrição do deus: ")
            livro_dos_deuses[nome] = descricao
            print(f"{nome} adicionado com sucesso.")

    elif escolha == "3":
        nome = input("Digite o nome do deus a ser atualizado: ")
        if nome in livro_dos_deuses:
            nova_desc = input("Nova descrição: ")
            livro_dos_deuses[nome] = nova_desc
            print(f"{nome} foi atualizado.")
        else:
            print("Deus não encontrado.")

    elif escolha == "4":
        print("\nTodos os deuses registrados:")
        for nome, descricao in livro_dos_deuses.items():
            print(f"{nome}: {descricao}")

    elif escolha == "6":
        print("Encerrando o Livro dos Deuses...")
        executando = False
    
    elif escolha == "5":
        print("Salvando alterações")
        with open("Desafio #9 - Enciclopedia dos Deuses Turbo/deuses.json", mode="w", encoding="UTF-8") as file:
            json.dump(livro_dos_deuses, file, ensure_ascii=False)
        print("Alterações salvas, até breve.")
        executando = False

    else:
        print("Opção inválida. Tente novamente.")


