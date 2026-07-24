import json


def carregar_produtos(caminho):
    try:
        with open(caminho, mode="r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as erro:
        print(f"JSON inválido na linha {erro.lineno}. O arquivo não será alterado.")
        return None


def validar_produto(produto):
    if not produto["nome"]:
        raise ValueError("O nome é obrigatório.")
    if produto["preco"] <= 0:
        raise ValueError("O preço deve ser maior que zero.")
    if produto["quantidade"] < 0:
        raise ValueError("A quantidade não pode ser negativa.")


def salvar_produtos(produtos, caminho):
    try:
        with open(caminho, mode="w", encoding="utf-8") as arquivo:
            json.dump(produtos, arquivo, ensure_ascii=False, indent=2)
        return True
    except OSError as erro:
        print(f"Não foi possível salvar: {erro}")
        return False


def main():
    caminho = "produtos.json"
    produtos = carregar_produtos(caminho)
    if produtos is None:
        return

    try:
        produto = {
            "nome": input("Nome: "),
            "preco": float(input("Preço: ")),
            "quantidade": int(input("Quantidade: ")),
        }
        validar_produto(produto)
    except ValueError as erro:
        print(f"Cadastro cancelado: {erro}")
        return

    produtos.append(produto)
    if salvar_produtos(produtos, caminho):
        print("Produto salvo.")


if __name__ == "__main__":
    main()
