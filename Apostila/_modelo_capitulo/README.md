# Modelo de pacote de capítulo

Este diretório é a base para cada encontro do curso. Copie a pasta completa, renomeie-a com prefixo numérico e substitua todos os marcadores entre colchetes.

Exemplo:

```text
_modelo_capitulo/
        ↓
01_primeiros_passos/
```

## Estrutura do pacote

```text
XX_nome_do_capitulo/
├── capitulo.md
├── imagens/
│   └── README.md
├── starter/
│   └── README.md
└── solucao/
    └── README.md
```

- `capitulo.md`: material autocontido do estudante.
- `imagens/`: capturas de tela e diagramas realmente necessários.
- `starter/`: arquivos fornecidos no início do encontro.
- `solucao/`: solução comentada, liberada somente após a tentativa e a correção.

## Regras de autoria

- Um capítulo corresponde a um encontro de quatro horas, incluindo o intervalo.
- O capítulo não depende dos arquivos produzidos no encontro anterior.
- O pacote inicial contém tudo que o estudante precisa para começar.
- Não há cronograma rígido por minutos.
- Não há roteiro, mapa ou metadados de slides.
- Cada bloco de código introduz, preferencialmente, uma única ideia nova.
- Todo exemplo executável informa a saída esperada.
- Toda imagem possui texto alternativo e instrução textual equivalente.
- Identificadores em português usam caracteres ASCII e `snake_case`.
- Soluções ficam fora do corpo da apostila.
- Os marcadores de orientação escritos como comentários HTML devem ser removidos na versão final.

## Checklist antes de considerar o pacote pronto

- [ ] Todos os marcadores entre colchetes foram substituídos.
- [ ] O capítulo pode ser iniciado sem código de outro encontro.
- [ ] Os objetivos são observáveis.
- [ ] Os exemplos foram executados no ambiente oficial.
- [ ] As saídas esperadas conferem com a execução real.
- [ ] Há pelo menos uma atividade de depuração.
- [ ] Há prática acompanhada, exercício independente e tarefa de saída.
- [ ] Os arquivos de `starter/` foram testados em uma cópia limpa.
- [ ] A solução foi testada separadamente.
- [ ] A solução não aparece no enunciado nem nas pistas.
- [ ] A política de IA está indicada corretamente.
- [ ] Não há dados pessoais, credenciais ou segredos.
- [ ] Links e capturas de tela foram verificados.

