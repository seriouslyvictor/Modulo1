import artwork, time

RECEITAS = {
    "espada": {
        "ingredientes": {
            "ferro": 3,
            "madeira": 1,
        },
        "custo": 10,
        "arte": artwork.espada
    },
    "escudo": {
        "ingredientes": {
            "ferro": 2,
            "madeira": 3,
        },
        "custo": 8,
        "arte": artwork.escudo
    },
    "arco": {
        "ingredientes": {
            "madeira": 4,
            "corda": 2,
        },
        "custo": 7,
        "arte": artwork.arco
    },
}

recursos = {
    "ferro": 10,
    "madeira": 10,
    "corda": 5,
}

ouro = 0

moedas = {
    "Moeda de Ouro": 1,
    "Moeda de Prata": 0.5,
    "Moeda de Cobre": 0.1,
}

def imprimir_relatorio():
    print("\n===== Relatório da Oficina =====")
    for material, qtd in recursos.items():
        print(f"{material.capitalize()}: {qtd}")
    print(f"Ouro ganho: {ouro} 💰")
    print("================================\n")

def atualizar_oficina(item):
    global ouro
    ingredientes = RECEITAS[item]["ingredientes"]
    for material in ingredientes:
        recursos[material] -= ingredientes[material]
    ouro += RECEITAS[item]["custo"]

def fabricar_item(item):
    receita = RECEITAS[item]["ingredientes"]
    for material, necessario in receita.items():
        if necessario > recursos.get(material, 0):
            print(f"Faltam recursos: {material} insuficiente para fabricar {item}!")
            return

    print(f"O custo para fabricar um(a) {item} é {RECEITAS[item]['custo']} ouro.")
    moedas_inseridas = []
    for moeda, valor in moedas.items():
        quantidade = int(input(f"Quantas {moeda}s você quer inserir? "))
        moedas_inseridas.append(quantidade * valor)

    total_pago = sum(moedas_inseridas)
    custo_item = RECEITAS[item]["custo"]

    if total_pago >= custo_item:
        troco = round(total_pago - custo_item, 2)
        atualizar_oficina(item)
        print("Clank! Clank! Clank!")
        time.sleep(1)
        print(f"✅ {item.capitalize()} fabricado com sucesso! ⚔️")
        time.sleep(1)
        print(RECEITAS[item]["arte"])
        if troco > 0:
            print(f"💰 Seu troco é {troco} ouro.")
    else:
        print("❌ Ouro insuficiente... Transação cancelada.")

def principal():
    ligada = True
    while ligada:
        escolha = input("O que deseja fabricar? (espada/escudo/arco) ou digite 'sair': ").lower()
        if escolha == "sair":
            print("🔧 Desligando a oficina...")
            ligada = False
        elif escolha == "inv":
            imprimir_relatorio()
        elif escolha in RECEITAS:
            fabricar_item(escolha)
        else:
            print("Comando inválido. Tente novamente.")

print("🏰 Bem-vindo à Oficina Medieval! 🪓")
print(artwork.splash)
print("Você pode fabricar: Espada, Escudo, Arco")
principal()
