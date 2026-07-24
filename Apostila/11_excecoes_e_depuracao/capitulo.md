# Capítulo 11 — Validação, exceções e depuração sistemática

Arquivos podem não existir, JSON pode estar incompleto e entradas podem não ser convertíveis. Um programa confiável não finge que essas situações nunca acontecerão: ele distingue falhas previsíveis de erros de programação e reage de forma clara.

Neste encontro, vamos aprofundar a leitura de erros e proteger operações específicas sem esconder problemas inesperados.

## Visão geral do encontro

| Item | Informação |
|---|---|
| Encontro | 11 de 15 |
| Duração agendada | 4 horas, incluindo intervalo |
| Tema central | Exceções específicas, validação e recuperação segura |
| Produto do encontro | Leitura e gravação robustas de um catálogo JSON |
| Uso de IA | Proibido neste encontro |

## Antes de começar

Copie `starter/` inteira. Ela contém arquivos válidos e inválidos para teste.

```text
starter/
├── captura_ampla.py
├── catalogo_base.py
├── produtos_corrompidos.json
├── produtos_validos.json
├── README.md
└── verificar_capitulo.py
```

Você precisa saber usar funções, módulos, dicionários e JSON.

## Objetivos de aprendizagem

- distinguir erro de sintaxe, execução e lógica;
- ler traceback de baixo para cima;
- proteger uma operação com `try`;
- capturar exceções específicas;
- tratar tipos diferentes separadamente;
- acessar detalhes com `as erro`;
- produzir `ValueError` com `raise`;
- validar dados antes da gravação;
- evitar `except:` genérico;
- testar caminhos de sucesso e falha.

## Três categorias úteis

### Erro de sintaxe

Python não consegue interpretar a estrutura:

```python
print("Produto cadastrado)
```

### Erro em tempo de execução

A estrutura é válida, mas uma operação falha:

```python
quantidade = int("dez")
```

### Erro de lógica

O programa termina, mas produz resultado incorreto:

```python
preco = 10
quantidade = 3
total = preco + quantidade  # deveria multiplicar
```

`try` trata exceções de execução. Ele não corrige automaticamente erros de lógica.

## Lendo um traceback

Comece pela última linha:

```text
ValueError: invalid literal for int() with base 10: 'dez'
```

Depois procure o arquivo e a linha mais próxima do seu próprio código. Leia a instrução indicada e compare os valores reais com os esperados.

Processo recomendado:

1. reproduza o problema;
2. leia tipo e mensagem final;
3. localize arquivo e linha;
4. formule uma hipótese;
5. inspecione valores com `print()` ou `type()`;
6. altere uma coisa;
7. execute novamente;
8. teste um caso que já funcionava.

## Protegendo com `try` e `except`

```python
try:
    quantidade = int(input("Quantidade: "))
    print(f"Quantidade registrada: {quantidade}")
except ValueError:
    print("Digite uma quantidade inteira.")
```

Coloque dentro de `try` apenas as operações que podem produzir a exceção que você pretende tratar.

> **Erro comum:** envolver o programa inteiro em um único `try`. Isso dificulta saber qual operação falhou.

## Exceções específicas em arquivos

```python
import json


def carregar_produtos(caminho):
    try:
        with open(caminho, mode="r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
        return []
    except json.JSONDecodeError as erro:
        print(f"JSON inválido na linha {erro.lineno}: {caminho}")
        return None
```

Os retornos comunicam situações diferentes:

- `[]` significa que o arquivo ainda não existe; podemos começar um catálogo vazio;
- `None` significa que o arquivo existe, mas não pôde ser carregado; o programa deve parar sem gravar.

O chamador verifica esse contrato sem precisar de retorno múltiplo:

```python
produtos = carregar_produtos("produtos.json")
if produtos is None:
    print("Operação cancelada para preservar o arquivo.")
```

Falhas diferentes recebem mensagens diferentes:

- `FileNotFoundError`: caminho não encontrado;
- `json.JSONDecodeError`: conteúdo não é JSON válido;
- `PermissionError`: acesso negado;
- `OSError`: outra falha do sistema de arquivos.

## Detalhes da exceção

```python
except json.JSONDecodeError as erro:
    print("JSON inválido.")
    print(f"Linha: {erro.lineno}; coluna: {erro.colno}")
```

`erro` é o objeto da exceção. Use detalhes que ajudem a agir; não despeje informações técnicas sem contexto para o usuário final.

## Tratamento básico de falhas de gravação

```python
def salvar_produtos(produtos, caminho):
    try:
        with open(caminho, mode="w", encoding="utf-8") as arquivo:
            json.dump(produtos, arquivo, ensure_ascii=False, indent=2)
        return True
    except PermissionError:
        print(f"Sem permissão para gravar: {caminho}")
        return False
    except OSError as erro:
        print(f"Falha ao gravar o arquivo: {erro}")
        return False
```

`True` e `False` permitem que o chamador saiba se a operação foi concluída.

Esse tratamento informa falhas esperadas, mas não torna a gravação atômica: o modo `w` ainda esvazia o arquivo ao abri-lo. Neste curso, a regra de proteção é chamar a gravação somente depois que a leitura e a validação tiverem sido concluídas com sucesso.

## Criando um erro de validação com `raise`

```python
def validar_produto(produto):
    if not isinstance(produto, dict):
        raise ValueError("O produto deve ser um dicionário.")
    if "nome" not in produto or not produto["nome"]:
        raise ValueError("O nome do produto é obrigatório.")
    if produto.get("preco", 0) <= 0:
        raise ValueError("O preço deve ser maior que zero.")
```

`raise` sinaliza que o valor viola uma regra. A função que chamou pode tratar:

```python
try:
    validar_produto(produto)
except ValueError as erro:
    print(f"Produto inválido: {erro}")
```

Não use exceções para substituir toda condicional. Elas são úteis quando uma operação não pode cumprir seu contrato.

## Por que evitar `except:`

```python
try:
    resultado = preco * quantiade
except:
    print("Preço inválido.")
```

O nome `quantiade` está errado e produz `NameError`, mas o `except:` esconde o defeito e culpa o preço. Capturas amplas transformam bugs em mensagens enganosas.

Prefira:

```python
try:
    preco = float(input("Preço: "))
except ValueError:
    print("Digite um preço numérico.")
```

## Prática acompanhada — Catálogo resistente

Abra `starter/catalogo_base.py` e implemente:

1. `carregar_produtos(caminho)` retornando `[]` para arquivo ausente e `None` para JSON inválido;
2. `validar_produto(produto)` com `raise ValueError`;
3. `salvar_produtos(produtos, caminho)` com retorno booleano;
4. testes com `produtos_validos.json`;
5. testes com `produtos_corrompidos.json`;
6. teste com `arquivo_que_nao_existe.json`;
7. teste de produto sem nome e preço zero.

Registre resultados esperados antes de executar.

> **Pausa sugerida:** este é um bom ponto para o intervalo.

## Oficina de depuração — O tratamento que esconde o bug

Execute `starter/captura_ampla.py` com um preço válido. O programa exibe `Preço inválido`, mas o verdadeiro problema é um nome digitado incorretamente no código.

Investigue:

1. Remova temporariamente o `try` / `except` e execute.
2. Qual exceção real aparece?
3. Qual linha contém o nome incorreto?
4. Qual operação realmente precisa de tratamento?
5. Restrinja o `try` à conversão e capture `ValueError`.

## Exercício independente — Cadastro seguro

Crie `cadastro_seguro.py` com:

- `carregar_produtos(caminho)`;
- `validar_produto(produto)`;
- `salvar_produtos(produtos, caminho)`;
- `main()` protegido pelo `__name__` guard.

O fluxo deverá carregar `produtos.json`, receber um produto, validar, adicionar e salvar. Trate:

- entrada numérica inválida;
- arquivo ausente como catálogo vazio;
- JSON inválido sem sobrescrevê-lo automaticamente;
- produto com nome vazio, preço não positivo ou quantidade negativa;
- falha de gravação.

Se o JSON estiver inválido, encerre sem gravar. Não use classes ou inteligência artificial.

Use o mesmo contrato da prática: depois de carregar, teste `if produtos is None:` e encerre `main()` com `return`. Não é necessário criar tuplas nem retornar mais de um valor.

## Resumo do capítulo

- Erros de sintaxe, execução e lógica exigem investigações diferentes.
- O traceback deve ser lido a partir do tipo e da mensagem final.
- `try` contém operações arriscadas específicas.
- `except` deve capturar exceções esperadas.
- Exceções diferentes merecem respostas diferentes.
- `as erro` oferece detalhes.
- `raise` comunica violação de uma regra.
- `except:` genérico pode esconder defeitos.
- Caminhos de falha também precisam ser testados.

## Verifique seu aprendizado

1. `try` corrige erros de lógica?
2. Por que começar pela última linha do traceback?
3. Qual diferença existe entre arquivo ausente e JSON inválido?
4. Por que um `try` pequeno é mais fácil de depurar?
5. Quando usar `raise ValueError`?
6. Qual risco existe em `except:`?

## Tarefa de saída

Crie uma função `converter_quantidade(texto)` que retorna um inteiro válido ou `None` quando a conversão falhar. Teste com `"12"`, `"0"` e `"doze"`.

## Vocabulário

| Termo | Significado |
|---|---|
| Exceção | Objeto que representa uma falha durante execução. |
| Traceback | Caminho de chamadas apresentado quando uma exceção não é tratada. |
| Tratamento | Resposta planejada a uma falha previsível. |
| `raise` | Instrução que produz uma exceção. |
| Contrato | Condições que uma função exige e resultados que promete. |
| Recuperação | Caminho seguro adotado depois de uma falha esperada. |

## Referências e continuidade

- [Erros e exceções — tutorial oficial](https://docs.python.org/3/tutorial/errors.html)
- [Exceções embutidas](https://docs.python.org/3/library/exceptions.html)

No próximo capítulo, transformaremos registros de produto em objetos que agrupam estado e comportamento.
