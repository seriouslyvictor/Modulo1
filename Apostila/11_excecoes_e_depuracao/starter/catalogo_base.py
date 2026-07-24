import json


def carregar_produtos(caminho):
    """Retorne uma lista, [] se não existir ou None se o JSON for inválido."""
    pass


def validar_produto(produto):
    """Use raise ValueError quando uma regra não for atendida."""
    pass


def salvar_produtos(produtos, caminho):
    """Retorne True quando salvar e False quando ocorrer uma falha esperada."""
    pass


def testar_carga():
    caminhos = [
        "produtos_validos.json",
        "produtos_corrompidos.json",
        "arquivo_que_nao_existe.json",
    ]
    for caminho in caminhos:
        resultado = carregar_produtos(caminho)
        print(caminho, resultado)


# Depois de implementar as funções, retire o comentário da chamada abaixo.
# testar_carga()
