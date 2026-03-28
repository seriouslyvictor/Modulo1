import artwork
receitas = {
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

#TODO#1 Criar o menu principal que deve conter as opções de fabricar um item, imprimir o relatório da oficina e sair do programa, você pode criar o menu usando um loop while e um input para receber a opção do usuário.
# O usuário só sai do sistema quando digitar a opção de sair.
# se o usuário digitar "inv", deve imprimir o inventário de recursos disponíveis e o ouro ganho até o momento.
# O usuário deve poder escolher fabricar qualquer item das receitas digitando o nome do item, por exemplo: "espada".


#TODO#2 Criar uma função para imprimir o relatório da oficina, essa função deve imprimir a quantiade de cada recurso disponível e o ouro ganho até o momento.

#TODO#3 Criar uma função chamada fabricar_item que recebe o nome do item a ser fabricado, verifica se os recursos necessários estão disponíveis e imprime o custo do item. Se os recursos não estiverem disponíveis, deve imprimir uma mensagem informando que faltam recursos.

#TODO#4 Crie uma função chamada receber_moedas que solicita ao usuário quantas moedas de ouro, prata e cobre ele deseja receber. A função deve atualizar o valor do ouro com base nas moedas recebidas. Essa função deve ser chamada dentro da função fabricar_item após verificar se os recursos estão disponíveis.

#TODO#5 Criar uma função chamada atualizar_estoque que recebe o nome do item fabricado, atualiza os recursos disponíveis e o ouro ganho. Essa função deve ser chamada após a fabricação de um item.

#TODO#6 Crie uma função chamada entregar_item que recebe o nome do item fabricado e imprime uma mensagem de entrega do item, incluindo a arte do item.
