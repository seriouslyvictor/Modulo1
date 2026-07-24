# Revisão por estudante iniciante — capítulos 1 a 12

Li o plano, os doze capítulos na ordem proposta e os materiais `starter/` e `solucao/` necessários para conferir se as atividades começam de um ponto possível. A linguagem é acolhedora, adulta e, em geral, explica antes de cobrar. O padrão de pacote independente, com verificador de ambiente, prática, depuração, exercício e tarefa de saída, ajuda muito quem perdeu uma aula.

## Questões bloqueadoras ou de alto impacto

1. **Plano de conteúdo — estrutura curricular de 15 capítulos / pacotes disponíveis.** O plano promete 15 encontros, Streamlit, publicação, projeto longo e uma política de IA que muda nos capítulos 14–15. Porém a apostila disponível termina no Capítulo 12. Para mim, estudante, isso deixa sem material justamente a continuação anunciada no fim do Capítulo 12 e torna impossível alcançar vários resultados esperados do plano. É preciso disponibilizar os capítulos 13–15 ou ajustar o plano, a carga horária, os resultados e a política de IA ao escopo de 12 capítulos.

2. **Capítulo 1 — “Oficina de depuração”.** `starter/mensagem_com_erro.py` está sintaticamente correto: as três chamadas de `print()` têm as aspas fechadas. O texto afirma que há um `SyntaxError` intencional e pede para comparar as aspas, mas nada falha ao executar. Na primeira aula, isso pode fazer o estudante achar que não sabe localizar um erro que não existe e também quebra a confiança no material. O arquivo inicial precisa conter de fato o erro mostrado/explicado, ou a oficina deve ser reescrita para o comportamento atual.

3. **Capítulo 12 — “Classe e instância”, “Classificando o estoque” e “Prática acompanhada”.** A classe inicial aceita três argumentos (`nome`, `preco`, `quantidade`), mas a classificação usa `self.estoque_minimo`, que ainda não existe; depois o capítulo manda incluí-lo no `__init__`, sem reapresentar uma versão completa da classe nem atualizar as criações anteriores. Ao copiar os exemplos em sequência, é fácil obter `AttributeError` ou `TypeError`. Para uma primeira experiência com objetos, cada mudança de modelo deve trazer o bloco completo atualizado e uma chamada compatível.

## Sugestões menores

- **Capítulo 1 — “Rota A” e “Rota B”.** Os comentários `CAPTURA PENDENTE` ficam visíveis no texto. As instruções escritas são suficientes para continuar, mas os marcadores parecem trabalho inacabado e os passos de instalação/seleção de interpretador são justamente os mais difíceis de recuperar sozinho. Inserir as capturas prometidas ou substituir os comentários por uma nota editorial fora da versão do estudante reduziria a insegurança.

- **Capítulo 6 — “Repetindo enquanto uma condição for verdadeira”.** O exemplo que repete `int(input(...))` para quantidade negativa é útil, mas uma entrada como `dez` encerra o programa antes da repetição. Como exceções só aparecem no Capítulo 11, basta explicitar que este exemplo pressupõe número inteiro e indicar que a recuperação de texto inválido virá mais adiante; assim não parece uma contradição quando o aluno testa livremente.

- **Capítulo 9 — “Exercício independente — Orçamento modular”.** O enunciado pede uma pasta nova com dois arquivos, enquanto o capítulo vinha reforçando “copie `starter/`” e execute na pasta aberta. Uma linha explícita dizendo para abrir a pasta `orcamento/` no VS Code e executar `python app.py` nela evitaria o `ModuleNotFoundError` mais provável para quem está retomando o encontro sozinho.

- **Plano de conteúdo — “Política de uso de inteligência artificial”.** A regra é clara para capítulos 1–13 e os capítulos 1–12 a repetem de modo consistente: IA é proibida no encontro e nos exercícios. Falta apenas uma orientação operacional para um aluno com dúvida legítima (por exemplo, pedir ajuda ao professor, consultar a seção anterior e registrar a tentativa), especialmente porque os capítulos em que IA seria permitida ainda não estão presentes.

## Capítulos sem problema relevante identificado

- **Capítulo 2 — Variáveis, textos, entrada e saída:** progressão suave; o `starter/` e a oficina de `NameError` correspondem ao texto.
- **Capítulo 3 — Tipos de dados, conversões e cálculos:** explica o limite de `input()` antes de pedir cálculo e oferece testes realizáveis.
- **Capítulo 4 — Decisões e regras de validação:** a ordem das regras é ensinada e praticada antes de ser cobrada.
- **Capítulo 5 — Listas e coleções ordenadas:** exemplos, `starter/` e exercício são compatíveis com o repertório disponível.
- **Capítulo 7 — Funções e decomposição de problemas:** a diferença entre `print()` e `return` é bem destacada; a oficina tem um defeito real e recuperável.
- **Capítulo 8 — Dicionários e registros estruturados:** a transição das listas paralelas é bem motivada e o exercício é viável.
- **Capítulo 10 — Arquivos de texto e JSON:** alerta corretamente para cópias e sobrescrita; os arquivos fornecidos permitem a prática proposta.
- **Capítulo 11 — Validação, exceções e depuração sistemática:** o fluxo de investigação é claro, os cenários válidos/corrompidos existem e a regra de não sobrescrever JSON inválido é compreensível.

## Veredito

A apostila é uma base didática forte para iniciantes e favorece retomada após ausência. Antes de uso em turma, eu corrigiria obrigatoriamente a oficina do Capítulo 1, a sequência de exemplos do Capítulo 12 e a divergência entre o plano de 15 encontros e os 12 pacotes realmente entregues.
