"""
Error Handling in Python - File Management Examples
==================================================

This file demonstrates error handling concepts using file operations,
since files are a great place to encounter real-world errors.
"""

import json
# =============================================================================
# 1. BASIC TRY/EXCEPT - Fundamentos
# =============================================================================

def leitura_basica():
    # Erro fatal: FileNotFoundError
    with open('Error/nonexistent.txt', 'r', encoding="utf-8") as f:
        content = f.read()
    return content
#leitura_basica()

def leitura_com_safeguards():
    #Bloco TRY, operação que pode gerar erro
    try:
        with open('Error/dados.txt', 'r', encoding="utf-8") as f:
            content = f.read()
        return content
    #Bloco EXCEPT, captura o erro e trata conforme necessário
    except:
        print("Erro na abertura do arquivo. Verifique se o arquivo existe.")
        # Tratativa: Criar um novo arquivo com conteúdo padrão
        with open('Error/dados.txt', 'w', encoding="utf-8") as f:
            f.write("Conteúdo padrão")
        return "Conteúdo padrão foi criado no arquivo."
# leitura_com_safeguards()
# =============================================================================
# 2. SPECIFIC EXCEPTIONS - Being Precise
# =============================================================================

def ler_json(arquivo):
    """Reading JSON with specific error handling"""
    try:
        with open(arquivo, 'r', encoding="UTF-8") as f:
            dados = json.load(f)
        return dados
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo} não foi encontrado.")
        return False
    
    except json.JSONDecodeError as e:
        print(f"Erro: O arquivo {arquivo} não é um JSON válido.")
        print(f"Detalhes: {e}")
        return False
    
    except PermissionError:
        print(f"Erro: Permissão negada para acessar {arquivo}.")
        return False
# ler_json('Error/fakejson.json')
# =============================================================================
# 3. MULTIPLE EXCEPTIONS - Mais tipos de erros
# =============================================================================

def atualizar_json(deuses, arquivo):
    try:
        with open(arquivo, 'w', encoding="utf-8") as f:
            json.dump(deuses, f, indent=4, ensure_ascii=False)
        print(f"Salvo com sucesso {len(deuses)} entrada(s) no {arquivo}")
        return True
    
    except PermissionError:
        print(f"Não foi possível salvar {arquivo} - Permissão negada.")
        return False
    
    except OSError as e:
        print(f"Erro de sistema: {e}")
        return False
    
    except TypeError as e:
        print(f"Dados não puderam ser convertidos em JSON: {e}")
        return False
# atualizar_json([{"nome": "Zeus"},{"nome": "Hera"}, {"nome": "Apollo"}], 'Error/deuses.json')

# =============================================================================
# 5. PRACTICAL EXAMPLES - Criando seus erros
# =============================================================================

def salvar_deus_validacao(deus):
    """Salva deuses em um arquivo JSON, validando os dados primeiro."""
    try:    
        if not isinstance(deus, dict) or 'nome' not in deus:
            raise ValueError("Cada deus deve ser um dicionário com a chave 'nome'.")
        if not isinstance(deus['nome'], str) or not deus['nome']:
            raise ValueError("O nome do deus deve ser uma string não vazia.")

    except ValueError as ve:
        print(f"Erro de validação: {ve}")
        return False
    return True

salvar_deus_validacao({"nome": 1213})  # Deve gerar ValueError
salvar_deus_validacao("Zeus")  # Deve gerar ValueError
salvar_deus_validacao({"nome":"Zeus"})  # Deve validar corretamente


print("Exemplo de erro de validação concluído.")