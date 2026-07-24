import json


def carregar_produtos(caminho):
    try:
        with open(caminho, mode="r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        return []
    except json.JSONDecodeError as erro:
        print(f"JSON inválido na linha {erro.lineno}, coluna {erro.colno}.")
        return None


def validar_produto(produto):
    if not isinstance(produto, dict):
        raise ValueError("O produto deve ser um dicionário.")
    if "nome" not in produto or not produto["nome"]:
        raise ValueError("O nome é obrigatório.")
    if produto.get("preco", 0) <= 0:
        raise ValueError("O preço deve ser maior que zero.")
    if produto.get("quantidade", -1) < 0:
        raise ValueError("A quantidade não pode ser negativa.")


def salvar_produtos(produtos, caminho):
    try:
        with open(caminho, mode="w", encoding="utf-8") as arquivo:
            json.dump(produtos, arquivo, ensure_ascii=False, indent=2)
        return True
    except PermissionError:
        print(f"Sem permissão para gravar: {caminho}")
        return False
    except OSError as erro:
        print(f"Falha ao gravar: {erro}")
        return False


def main():
    print(carregar_produtos("produtos_validos.json"))
    print(carregar_produtos("produtos_corrompidos.json"))
    print(carregar_produtos("arquivo_que_nao_existe.json"))

    for produto_teste in [
        {"nome": "Caneta", "preco": 3.20, "quantidade": 4},
        {"nome": "", "preco": 3.20, "quantidade": 4},
        {"nome": "Caneta", "preco": 0, "quantidade": 4},
    ]:
        try:
            validar_produto(produto_teste)
            print("Produto válido.")
        except ValueError as erro:
            print(f"Produto inválido: {erro}")


if __name__ == "__main__":
    main()
