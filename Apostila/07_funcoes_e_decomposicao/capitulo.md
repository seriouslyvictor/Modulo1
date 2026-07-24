# Capítulo 7 — Funções e decomposição de problemas

Quando uma operação aparece várias vezes ou um programa começa a misturar entrada, cálculos, validações e mensagens, fica difícil localizar responsabilidades. Funções permitem dar nome a uma operação e executá-la quando necessário.

Neste encontro, vamos dividir regras de inventário em blocos pequenos, reutilizáveis e testáveis.

## Visão geral do encontro

| Item | Informação |
|---|---|
| Encontro | 7 de 15 |
| Duração agendada | 4 horas, incluindo intervalo |
| Tema central | Definição, parâmetros, retorno e composição de funções |
| Produto do encontro | Um resumo de produto organizado em funções |
| Uso de IA | Proibido neste encontro |

## Antes de começar

Este capítulo é autocontido. Copie `starter/` e abra a cópia no VS Code.

```text
starter/
├── funcoes_base.py
├── README.md
├── retorno_incorreto.py
└── verificar_capitulo.py
```

Você precisa reconhecer variáveis, condicionais, listas, laços e cálculos.

## Objetivos de aprendizagem

- definir e chamar funções;
- diferenciar definição de execução;
- usar parâmetros e argumentos;
- retornar valores;
- diferenciar `print()` de `return`;
- reconhecer variáveis locais;
- compor funções pequenas;
- verificar funções com casos de teste manuais;
- escolher responsabilidades claras para cada função.

## Definindo e chamando

```python
def exibir_cabecalho():
    print("=== CONTROLE DE ESTOQUE ===")
```

Essa definição prepara a função, mas não executa seu bloco. Para executar:

```python
exibir_cabecalho()
```

Os parênteses fazem parte da chamada.

```text
def nome_da_funcao():
    instruções

nome_da_funcao()
```

> **Erro comum:** definir corretamente e esperar uma saída sem chamar a função.

## Parâmetros e argumentos

Uma função pode receber informações:

```python
def exibir_produto(nome):
    print(f"Produto: {nome}")

exibir_produto("Caderno")
exibir_produto("Caneta")
```

`nome` é o parâmetro da definição. `"Caderno"` e `"Caneta"` são argumentos usados nas chamadas.

Com mais de um parâmetro:

```python
def exibir_estoque(nome, quantidade):
    print(f"{nome}: {quantidade} unidades")

exibir_estoque("Caderno", 8)
```

A ordem dos argumentos deve corresponder à ordem dos parâmetros.

## Produzindo um valor com `return`

```python
def calcular_custo(quantidade, preco_unitario):
    return quantidade * preco_unitario

custo = calcular_custo(12, 8.50)
print(f"Custo: R$ {custo:.2f}")
```

`return` encerra a função e entrega um valor ao ponto da chamada. Esse valor pode ser armazenado, comparado ou passado a outra função.

### `print()` não substitui `return`

```python
def calcular_custo_incorreto(quantidade, preco_unitario):
    print(quantidade * preco_unitario)

resultado = calcular_custo_incorreto(12, 8.50)
print(resultado)
```

Saída:

```text
102.0
None
```

A função exibiu o cálculo, mas não devolveu um resultado. Funções sem `return` explícito retornam `None`.

Use `print()` quando a responsabilidade é apresentar algo. Use `return` quando outra parte do programa precisa do valor.

## Variáveis locais

Variáveis criadas dentro de uma função são locais:

```python
def calcular_custo(quantidade, preco_unitario):
    total = quantidade * preco_unitario
    return total
```

`total` existe durante aquela chamada. Tentar usar `total` fora da função produz `NameError`.

Parâmetros também são nomes locais. Isso ajuda funções a trabalhar sem depender de variáveis espalhadas pelo programa.

> **Dica:** prefira receber dados por parâmetros e entregar resultados por `return`.

## Funções com decisões

```python
def classificar_estoque(quantidade, estoque_minimo):
    if quantidade < 0 or estoque_minimo < 0:
        return "inválido"
    if quantidade == 0:
        return "esgotado"
    if quantidade <= estoque_minimo:
        return "crítico"
    return "adequado"
```

Cada `return` encerra a chamada. Por isso, depois de rejeitar um caso, a função pode continuar com verificações simples.

```python
situacao = classificar_estoque(3, 5)
print(situacao)
```

## Compondo funções

Composição acontece quando uma função usa o resultado de outra:

```python
def calcular_custo(quantidade, preco_unitario):
    return quantidade * preco_unitario

def formatar_moeda(valor):
    return f"R$ {valor:.2f}"

custo = calcular_custo(12, 8.50)
mensagem = formatar_moeda(custo)
print(mensagem)
```

Cada função responde a uma pergunta pequena. Isso facilita leitura e teste.

## Testando manualmente

Uma função pode ser verificada sem executar o programa inteiro:

```python
print(classificar_estoque(-1, 5))  # esperado: inválido
print(classificar_estoque(0, 5))   # esperado: esgotado
print(classificar_estoque(3, 5))   # esperado: crítico
print(classificar_estoque(8, 5))   # esperado: adequado
```

Antes de executar, registre a entrada e o resultado esperado. Depois compare com o resultado observado.

| Quantidade | Mínimo | Esperado |
|---:|---:|---|
| `-1` | `5` | inválido |
| `0` | `5` | esgotado |
| `3` | `5` | crítico |
| `8` | `5` | adequado |

## Prática acompanhada — Funções do inventário

Abra `starter/funcoes_base.py` e complete:

1. `calcular_custo(quantidade, preco_unitario)`, que retorna o produto dos valores;
2. `classificar_estoque(quantidade, estoque_minimo)`, que retorna uma classificação;
3. `exibir_resumo(nome, quantidade, custo, situacao)`, que apresenta os dados;
4. chamadas com dados fornecidos no arquivo.

Mantenha cálculo, decisão e apresentação em funções diferentes.

Saída esperada:

```text
Produto: Caderno
Quantidade: 3
Custo: R$ 25.50
Situação: crítico
```

> **Pausa sugerida:** este é um bom ponto para o intervalo.

## Oficina de depuração — O valor que virou `None`

Abra `starter/retorno_incorreto.py`:

```python
def calcular_custo(quantidade, preco_unitario):
    print(quantidade * preco_unitario)

custo = calcular_custo(4, 5.0)
print(f"Dobro do custo: {custo * 2}")
```

A função exibe `20.0`, mas a multiplicação seguinte falha porque `custo` recebeu `None`.

Investigue:

1. Qual valor foi exibido dentro da função?
2. Qual valor foi entregue à variável `custo`?
3. Use `print(type(custo))` para confirmar.
4. A responsabilidade da função é exibir ou produzir o custo?
5. Qual palavra deve substituir `print` dentro da função?

## Exercício independente — Resumo funcional de produto

Crie `resumo_produto.py` com as funções:

- `calcular_valor_estoque(quantidade, preco)`: retorna o valor total;
- `classificar_estoque(quantidade, minimo)`: retorna `inválido`, `esgotado`, `crítico` ou `adequado`;
- `exibir_resumo(nome, quantidade, valor, situacao)`: apresenta os dados.

Depois:

1. receba nome, quantidade, preço e mínimo;
2. chame as funções;
3. apresente o resumo;
4. teste os quatro caminhos da classificação.

Não use módulos, dicionários ou inteligência artificial.

<details>
<summary>Pista</summary>

Guarde cada retorno em uma variável antes de chamar `exibir_resumo`.

</details>

## Resumo do capítulo

- `def` cria uma função.
- A definição não executa a função.
- Parâmetros recebem argumentos.
- `return` entrega um resultado.
- `print()` apresenta; `return` permite reutilizar.
- Funções sem retorno explícito produzem `None`.
- Variáveis locais existem no contexto da chamada.
- Funções pequenas podem ser compostas.
- Casos manuais verificam comportamento isolado.

## Verifique seu aprendizado

1. Qual diferença existe entre definir e chamar?
2. O que diferencia parâmetro de argumento?
3. Quando usar `return`?
4. Por que uma função que apenas imprime pode produzir `None`?
5. O que significa uma variável ser local?
6. Como testar uma função de classificação sem executar todo o sistema?

## Tarefa de saída

Crie uma função `calcular_total(quantidade, preco)` que retorna o resultado. Chame-a com dois pares de valores e compare as saídas com cálculos manuais.

## Vocabulário

| Termo | Significado |
|---|---|
| Função | Bloco nomeado e reutilizável. |
| Parâmetro | Nome recebido pela definição. |
| Argumento | Valor fornecido na chamada. |
| Retorno | Valor entregue por `return`. |
| `None` | Ausência de um valor produzido. |
| Escopo local | Região em que um nome criado na função está disponível. |
| Composição | Uso do resultado de uma função por outra operação. |

## Referências e continuidade

- [Definindo funções — tutorial oficial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

No próximo capítulo, representaremos cada produto como um registro com campos nomeados usando dicionários.

