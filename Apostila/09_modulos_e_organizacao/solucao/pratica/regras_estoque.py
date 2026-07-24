def calcular_valor(quantidade, preco):
    return quantidade * preco


def classificar(quantidade, minimo):
    if quantidade < 0 or minimo < 0:
        return "inválido"
    if quantidade == 0:
        return "esgotado"
    if quantidade <= minimo:
        return "crítico"
    return "adequado"

