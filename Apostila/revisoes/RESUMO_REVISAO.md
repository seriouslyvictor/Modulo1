# Consolidação das revisões — capítulos 1 a 12

Os pareceres foram produzidos após a entrega dos doze pacotes e foram preservados sem alterações:

- `feedback_estudante.md`: leitura simulada por estudante iniciante, usando Terra;
- `feedback_instrutor.md`: revisão técnica e didática por instrutor experiente, usando Sol.

## Correções incorporadas

- Capítulo 4: a solução agora rejeita status diferentes de `ativo` e `inativo`.
- Capítulo 6: o exemplo com `while` declara que a recuperação de texto não numérico será ensinada com exceções.
- Capítulo 8: o desempacotamento de cada par retornado por `items()` passou a ser explicado.
- Capítulo 9: o exercício modular informa de qual pasta executar `python app.py`.
- Capítulo 11: arquivo ausente retorna `[]`, JSON inválido retorna `None`, e o chamador interrompe o fluxo antes da gravação.
- Capítulo 11: capítulo, starter e soluções usam o mesmo contrato sem retorno múltiplo ou tuplas.
- Capítulo 11: “gravação segura” foi substituída por “tratamento básico de falhas de gravação”, com a limitação do modo `w` explícita.
- Capítulos 11 e 12: os starters receberam assinaturas, checkpoints e testes orientadores sem revelar as implementações.
- Capítulo 12: a evolução de `Produto` reapresenta a classe completa ao adicionar `estoque_minimo` e atualiza as instanciações.
- Capítulo 12: a oficina explica com precisão que `self` é uma convenção e que o primeiro parâmetro recebe a instância.
- Plano: foi removida a indexação de strings que estava prometida, mas não era ensinada nem necessária.

## Observações avaliadas e não tratadas como defeitos desta entrega

- O plano continua com 15 capítulos, enquanto esta entrega termina no 12, porque o escopo solicitado foi produzir até o Capítulo 12. Os capítulos 13–15 permanecem como continuidade planejada.
- O `SyntaxError` do Capítulo 1 existe no arquivo `starter/mensagem_com_erro.py`; a observação contrária do parecer estudantil não se confirmou na verificação do arquivo.
- A extensão dos capítulos não foi uniformizada. A decisão editorial do curso permite encontros com densidades diferentes, sem impor a mesma quantidade de texto ou de atividades a todos.

## Pendências editoriais antes da distribuição em sala

- Capturar e validar as quatro telas reais do Windows indicadas no Capítulo 1, sem dados pessoais e com texto alternativo.
- Pilotar especialmente os capítulos 1–4 com cronômetro e marcar trechos opcionais se a turma não concluir o núcleo no encontro.
- Antes de redigir os capítulos 13–15, aplicar o recorte recomendado no parecer do instrutor para composição, Streamlit, Git e publicação.

## Verificação posterior às correções

- 87 arquivos Python analisados sintaticamente com sucesso.
- O único arquivo Python inválido é o erro de aspas intencional do Capítulo 1.
- O contrato do Capítulo 11 foi testado: arquivo ausente produz `[]` e JSON corrompido produz `None`.
- A solução do Capítulo 4 foi testada com status desconhecido e o rejeita explicitamente.
- Os blocos Markdown dos capítulos alterados permanecem com cercas balanceadas.
