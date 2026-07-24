# Parecer de revisão instrucional — Capítulos 1 a 12

## Veredito geral

**Ainda não está pronto para avançar sem correções aos Capítulos 13–15.** A sequência conceitual é boa e a maior parte dos exemplos e soluções está tecnicamente correta, mas há bloqueios didáticos importantes: o Capítulo 11 exige na solução um protocolo de retorno não ensinado e explicitamente fora do núcleo; a carga dos Capítulos 1–4 não é realista para iniciantes em encontros de 3h45 de atividade; os *starters* dos Capítulos 11 e 12 oferecem pouco apoio para práticas grandes; e o plano dos Capítulos 14–15 concentra interface, ambiente, Git, aplicação completa e publicação em apenas dois encontros.

O Capítulo 13 pode ser produzido depois de corrigidos os bloqueios de transição dos Capítulos 11–12. Para os Capítulos 14–15, é necessário antes reduzir escopo, fornecer um ponto de partida substancial ou reservar preparação fora do encontro.

## Achados de alta severidade

### 1. O exercício do Capítulo 11 depende de um contrato de retorno não ensinado e fora do escopo

**Evidência:** em `11_excecoes_e_depuracao/capitulo.md`, seção **Exceções específicas em arquivos**, linhas 117–126, `carregar_produtos()` devolve `[]` tanto para arquivo ausente quanto para JSON inválido. A prática acompanhada, linhas 207–219, repete esse mesmo contrato. Porém, o exercício independente exige distinguir os casos: arquivo ausente vira catálogo vazio, enquanto JSON inválido deve encerrar sem gravação (linhas 235–252).

A solução cria uma técnica nova em `11_excecoes_e_depuracao/solucao/cadastro_seguro.py`, linhas 4–12 e 34–38: retorna e desempacota tuplas como `([], True)` e `([], False)`. Tuplas estão classificadas como “opcional ou fora do núcleo” em `PLANO_CONTEUDO.md`, linhas 533–555. O estudante precisa inventar simultaneamente um protocolo de estado, retorno múltiplo e desempacotamento para resolver o exercício.

**Impacto:** o exercício mede descoberta de uma técnica não ensinada, não apenas tratamento de exceções. Além disso, o exemplo anterior normaliza dois estados semanticamente diferentes para `[]`, o que prepara o estudante para sobrescrever acidentalmente um JSON corrompido.

**Ação recomendada:** ensinar antes do exercício um contrato explícito usando recursos do núcleo, por exemplo `None` para “não pode continuar” e `[]` para “arquivo ausente”, ou incluir formalmente retorno múltiplo e desempacotamento no currículo. A prática deve demonstrar exatamente a distinção que o exercício cobra.

### 2. A carga dos Capítulos 1–4 não cabe com segurança em quatro horas para o público declarado

O curso prevê 3h45 de atividade por encontro (`PLANO_CONTEUDO.md`, linhas 36–45), incluindo explicação, prática acompanhada, depuração, exercício independente, correção e tarefa de saída. Contudo, há uma diferença muito grande de densidade:

| Capítulo | Linhas | Palavras aproximadas | Blocos de código | Objetivos |
|---|---:|---:|---:|---:|
| 1 | 600 | 3.013 | 24 | 7 |
| 2 | 629 | 2.560 | 37 | 8 |
| 3 | 674 | 2.666 | 44 | 8 |
| 4 | 673 | 2.777 | 35 | 8 |
| 5–12 | 286–372 | 1.039–1.320 | 10–26 | 8–10 |

No Capítulo 1, somente as duas rotas de ambiente ocupam as linhas 94–246; depois ainda vêm primeira programação, terminal, prática, depuração, exercício e saída. Em laboratório real, instalação, permissões, interpretadores e diferenças entre `python` e `py` produzem variação de tempo justamente entre os estudantes que mais precisam de apoio.

Os Capítulos 3 e 4 acumulam muitos conceitos novos em um encontro: o Capítulo 3 cobre quatro tipos, cinco conversões, operadores, três divisões, precedência, separador numérico e formatação; o Capítulo 4 cobre comparações, três ramos condicionais, indentação, três operadores lógicos, agrupamento, pertencimento e ordem de regras.

**Ação recomendada:** pilotar com cronômetro e definir conteúdo essencial versus leitura/atividade opcional. No Capítulo 1, tratar a instalação doméstica como demonstração ou roteiro para casa, preservando em aula a verificação do laboratório. Nos Capítulos 2–4, reduzir exemplos repetidos ou mover extensões (`bool()`, `_` numérico, agrupamentos complexos) para boxes opcionais.

### 3. Os *starters* dos Capítulos 11–12 não oferecem andaime suficiente para a prática proposta

`11_excecoes_e_depuracao/starter/catalogo_base.py` tem 17 linhas e apenas três funções com `pass`; sua solução, `solucao/catalogo_resistente.py`, tem 54 linhas, vários caminhos de exceção, validação, testes e o uso novo de `isinstance()`. Já `12_objetos_estado_comportamento/starter/produto_base.py` tem 7 linhas, enquanto a prática pede nove entregas (linhas 234–248 do capítulo) e a solução `solucao/produto.py` tem 56 linhas.

**Impacto:** após capítulos altamente guiados, o estudante encontra de repente uma página quase vazia para produzir duas das abstrações mais difíceis do curso. Isso aumenta cópia da solução e reduz a evidência de aprendizagem.

**Ação recomendada:** fornecer assinaturas, chamadas de teste e checkpoints intermediários nos *starters*. No Capítulo 12, separar a prática em uma primeira versão com `__init__` e consulta, seguida de métodos de alteração e validação. No Capítulo 11, fornecer a matriz “situação → retorno → pode salvar?” antes da implementação.

### 4. O plano dos Capítulos 13–15 está acima da capacidade restante do curso

O Capítulo 13 prevê composição, listas de objetos, responsabilidade, atributos de classe, `@classmethod`, atributos internos, conversão objeto–dicionário e separação de domínio (`PLANO_CONTEUDO.md`, linhas 322–343). O Capítulo 14 acrescenta `.venv`, instalação, modelo de rerun do Streamlit, vários widgets, formulários, layout, Session State, integração com objetos e criação de contas (`PLANO_CONTEUDO.md`, linhas 345–369). O Capítulo 15 exige CRUD completo, Git desde o início, GitHub, dependências, publicação, logs e apresentação (`PLANO_CONTEUDO.md`, linhas 371–407).

Para iniciantes absolutos, os dois encontros do “projeto longo” não oferecem tempo real para projetar, implementar, depurar, compreender Git e publicar. O risco é a aplicação final virar montagem guiada ou código gerado por IA que o estudante não consegue explicar, contrariando a política das linhas 501–511.

**Ação recomendada:** manter o Capítulo 13 estritamente em composição e serialização; retirar `@classmethod` e atributos de classe do núcleo se não forem indispensáveis. Entregar no Capítulo 14 um domínio já funcional e um ambiente previamente validado. Para o Capítulo 15, fornecer repositório inicial, checklist de publicação e uma versão mínima obrigatória menor; recursos de busca, filtro e atualização podem ser incrementos.

### 5. O Capítulo 1 ainda contém recursos visuais obrigatórios pendentes

O plano exige capturas anotadas (`PLANO_CONTEUDO.md`, linhas 70–91). O capítulo contém quatro marcadores `CAPTURA PENDENTE` nas linhas 110, 179, 196 e 224, e `01_primeiros_passos/imagens/` possui apenas `README.md`, sem as imagens.

As instruções textuais são utilizáveis, e a orientação sobre Python Install Manager e VS Code User Installer está de acordo com a documentação oficial consultada em 22/07/2026. Ainda assim, seleção de interpretador, extensão correta e botão de execução são os pontos em que iniciantes mais dependem de localização visual.

**Ação recomendada:** não considerar o pacote pronto para distribuição até produzir e validar as quatro capturas no Windows do curso, com alternativa textual e sem dados pessoais.

## Achados de média severidade

### 6. A oficina de `self` ensina uma regra imprecisa

Em `12_objetos_estado_comportamento/capitulo.md`, linhas 252–274, o texto afirma que “`self` foi omitido”. Tecnicamente, `self` não é palavra reservada nem nome obrigatório; o problema do arquivo `starter/self_incorreto.py` é que a assinatura tem apenas três parâmetros no total. O primeiro, chamado `nome`, recebe a instância automaticamente, e a chamada fornece três argumentos adicionais, causando `TypeError: Produto.__init__() takes 3 positional arguments but 4 were given`.

**Ação recomendada:** explicar que métodos de instância precisam de um primeiro parâmetro para receber a instância e que `self` é a convenção obrigatória do curso, embora não seja exigido pela sintaxe. Rastrear explicitamente a associação dos argumentos. Isso evita que o estudante memorize a falsa regra “Python procura a palavra `self`”.

### 7. Há uma promessa de normalização de texto que nunca é cumprida

`04_condicionais_e_validacao/capitulo.md`, linha 575, afirma que normalização de maiúsculas e espaços será tratada quando operações de texto forem aprofundadas. Nos Capítulos 5–12 não há ensino de `.lower()`; `.strip()` aparece apenas incidentalmente na leitura de linhas do Capítulo 10 (linhas 78–88), sem conexão com entrada do usuário.

Esse vazio reaparece no Capítulo 12: `if not nome` rejeita string vazia, mas aceita `"   "`. A interface Streamlit dos capítulos finais precisará justamente normalizar e validar entradas.

**Ação recomendada:** incluir uma seção curta de normalização antes do projeto, ou remover a promessa e declarar explicitamente a restrição. O mesmo contrato deve aparecer nas soluções de validação.

### 8. O plano promete indexação de strings no Capítulo 3, mas o capítulo não a ensina

`PLANO_CONTEUDO.md`, linhas 116–136, inclui “indexação básica de strings”. Não há exemplo ou objetivo correspondente em `03_tipos_e_calculos/capitulo.md`.

**Ação recomendada:** retirar esse item do plano, pois não é necessário para os exercícios, ou acrescentar um exemplo mínimo e uma evidência de aprendizagem. Não deixar conteúdo contratado apenas no plano.

### 9. “Gravação segura” é uma descrição forte demais para `open(..., "w")`

`11_excecoes_e_depuracao/capitulo.md`, linhas 146–160, chama de **Gravação segura** uma função que abre diretamente o arquivo definitivo com `w`. O próprio Capítulo 10 ensinou que isso trunca imediatamente o conteúdo. O `try` trata algumas falhas, mas não torna a atualização atômica nem preserva o arquivo anterior se ocorrer falha após a abertura.

**Ação recomendada:** para manter o nível introdutório, renomear para “tratamento básico de falhas de gravação” e dizer explicitamente qual risco permanece. Gravação temporária seguida de substituição pode ficar fora do núcleo.

### 10. Desempacotamento aparece sem modelo mental suficiente

`08_dicionarios_e_registros/capitulo.md`, linhas 128–135, usa `for chave, valor in produto.items()`, mas não explica por que dois nomes recebem cada item. Essa omissão se torna relevante porque o Capítulo 11 usa novamente desempacotamento em uma situação mais difícil.

**Ação recomendada:** rastrear uma iteração de `items()` e nomear o mecanismo como desempacotamento de um par, sem precisar transformar tuplas em conteúdo amplo do núcleo.

### 11. Status inválido é silenciosamente classificado como “inativo”

O exercício do Capítulo 4 pede `ativo` ou `inativo` (`capitulo.md`, linhas 526–575), mas `solucao/consulta_disponibilidade.py`, linha 10, usa `elif status != "ativo"`. Assim, `"ativoo"`, string vazia ou qualquer outro texto vira “produto inativo”.

**Ação recomendada:** validar pertencimento a `ativo`/`inativo` ou deixar explícito que os testes pressupõem entrada válida e que a solução não valida esse campo. Como o tema é validação, a primeira opção é pedagogicamente mais coerente.

### 12. Exemplos executáveis voltam a produzir efeitos ao importar

O Capítulo 9 ensina a proteger testes demonstrativos com o `__name__` guard (`09_modulos_e_organizacao/capitulo.md`, linhas 165–201). Entretanto, `11_excecoes_e_depuracao/solucao/catalogo_resistente.py`, linhas 40–53, e as soluções principais do Capítulo 12 (`produto.py`, `produto_controlado.py` e `categoria.py`) executam demonstrações no nível do módulo.

**Ação recomendada:** se esses arquivos forem apresentados como scripts, declarar isso. Se forem base para o Capítulo 13, colocar demonstrações em `main()` para reforçar a convenção já ensinada e evitar saída inesperada durante importação.

## Avaliação por pacote

| Capítulo | Parecer sobre capítulo, *starter* e solução |
|---|---|
| 1 | Conceitos e exercício se alinham; erro de aspas é apropriado. Carga excessiva e quatro capturas pendentes impedem fechamento editorial. |
| 2 | Sequência variável → entrada → composição de texto é clara; `NameError`, prática, exercício e solução estão alinhados. Densidade ainda alta para o primeiro contato com estado. |
| 3 | Explicações sobre `input()`, conversão, `bool("False")`, divisões e erro lógico estão corretas; soluções respeitam as restrições. Falta a indexação de strings prometida e há excesso de tópicos. |
| 4 | Boa ênfase na ordem de condições e em erro lógico sem traceback. Exercício e solução se alinham nos casos fornecidos, mas não tratam status fora do contrato. |
| 5 | Pacote coeso, carga plausível e boa oficina de `IndexError`; prática e soluções correspondem ao enunciado. |
| 6 | Progressão `for` → acumuladores → listas paralelas → `while` é correta; o risco de tamanhos diferentes é explicitado. Saídas e contagens das soluções conferem. |
| 7 | Distinção `print()`/`return` e oficina de `None` são pedagogicamente fortes. *Starter*, exercício e soluções estão alinhados. |
| 8 | Modelo lista de dicionários prepara bem persistência. Falta explicar o desempacotamento de `items()`; demais soluções e cálculos conferem. |
| 9 | Boa separação entre regra e interação e boa oficina de efeito na importação. Estrutura de pastas da solução corresponde às quatro atividades. |
| 10 | Caminho relativo, UTF-8 e risco do modo `w` são explicados corretamente. A oficina é destrutiva, mas o texto e README exigem cópia descartável. Soluções dependem corretamente do diretório de execução indicado. |
| 11 | Tipos de erro, `try` pequeno e captura específica são bons. O contrato de carga, o salto para tuplas e a noção de gravação segura precisam ser corrigidos antes de avançar. |
| 12 | A abordagem “estado + comportamento” e composição como próximo passo estão alinhadas ao plano. O *starter* é insuficiente e a explicação da oficina de `self` precisa de precisão técnica. |

## Verificações técnicas realizadas

- Foram analisados sintaticamente 88 arquivos `.py` dos pacotes. Todos são válidos, exceto `01_primeiros_passos/starter/mensagem_com_erro.py`, cujo `SyntaxError` é intencional.
- Os cinco JSON destinados ao caminho de sucesso são válidos. Os dois `produtos_corrompidos.json` do Capítulo 11 falham intencionalmente na linha 2, coluna 54.
- Para todos os capítulos existe correspondência nominal entre prática, oficina, exercício independente, tarefa de saída e os arquivos listados nos READMEs de `starter/` e `solucao/`.
- Os resultados numéricos e classificações das soluções dos Capítulos 3, 4, 6, 7 e 8 conferem com os exemplos e casos de teste dos capítulos.
- As instruções atuais do Capítulo 1 sobre o Python Install Manager foram conferidas com a [documentação oficial do Python para Windows](https://docs.python.org/3/using/windows.html), e a existência do instalador de usuário foi conferida com a [documentação oficial do VS Code para Windows](https://code.visualstudio.com/docs/setup/windows).

## Pontos fortes a preservar

- Progressão concreta: textos → tipos → decisões → coleções → repetição → funções → registros → módulos → persistência → exceções → objetos.
- Domínio de inventário reduz vocabulário sem introduzir dependências externas.
- Oficinas de erro cobrem sintaxe, nome, tipo, lógica, índice, acumulador, retorno, chave, importação, modo de arquivo, captura ampla e métodos.
- Separação entre *starter* e solução está consistente; os capítulos não dependem do código salvo na aula anterior.
- O curso evita herança artificial e prepara composição, que é a escolha correta para o Capítulo 13.

## Decisão de continuidade

**Capítulo 13:** prosseguir somente após corrigir o contrato do Capítulo 11, reforçar a oficina e o *starter* do Capítulo 12 e decidir como os objetos serão convertidos para dicionários sem introduzir abstrações extras.

**Capítulos 14–15:** não prosseguir com o escopo atual sem um recorte de versão mínima, *starter* funcional, preparação prévia de contas/ambiente e um ensaio cronometrado do fluxo completo até a publicação.

**Parecer final:** base conceitual promissora e majoritariamente correta, porém **aprovada com correções obrigatórias antes da continuidade e ainda não pronta para aplicação integral em sala**.
