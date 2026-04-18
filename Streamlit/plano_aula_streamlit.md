# 🌐 Plano de Aula — Interfaces Web com Python e Streamlit
**Foco em Apps com IA e APIs | Curso Python Generalista**

| Duração total | Público | Pré-requisito |
|---|---|---|
| 6 horas | Ensino médio público, adolescentes | `def`, `return`, `pip install` básicos |

---

## Visão Geral da Aula

| Bloco | Tema | Duração |
|---|---|---|
| 1 | O que é Streamlit? Primeiros Widgets | 1h |
| 2 | Interatividade: Botões, Inputs e Lógica | 1h |
| 3 | Conectando com APIs Externas | 1h30 |
| 4 | Projeto Guiado: FoodGrader com IA | 1h30 |
| 5 | Desafios e Deploy Gratuito | 1h |

---

## Por que Streamlit? O que dá pra fazer com isso?

### A conversa honesta antes de começar

Antes de instalar qualquer coisa, bora entender por que a gente escolheu essa ferramenta — e não outra.

Até agora no curso vocês aprenderam a lógica do Python: funções, loops, condições. Tudo isso rodava no terminal, sem cara, sem botão, sem visual. Ninguém ia mostrar isso pra um entrevistador e impressionar alguém, né?

O Streamlit resolve exatamente isso. Com ele, qualquer script Python vira um app com visual, que abre no navegador, que você manda o link pra alguém e a pessoa já usa — sem instalar nada. E o mais importante: sem precisar aprender HTML, CSS ou JavaScript. Só Python.

### Onde o Streamlit aparece de verdade no mercado

Quando você entrar em qualquer estágio ou trainee — em TI, em administração, em finanças, onde for — vai ter alguém com uma planilha enorme que precisaria de automação, ou um processo chato que a IA poderia agilizar, ou um relatório que precisaria virar algo interativo.

Com Streamlit, você consegue entregar isso. Um estagiário que chega com um app funcionando já na primeira semana chama atenção de um jeito que ninguém que só sabe Excel consegue. Não precisa ser perfeito. Precisa funcionar e resolver um problema real.

Na prática, Streamlit é muito usado em:

- Ferramentas internas de empresas — dashboards, relatórios automatizados, formulários com IA
- Prototipagem rápida — quando uma equipe quer testar uma ideia antes de contratar um dev front-end
- Ciência de dados e IA — mostrar modelos funcionando para quem não entende de código
- Projetos de portfólio — apps publicados na internet com URL pública, prontos para mostrar em entrevista

### As vantagens que importam pra vocês agora

- **Velocidade** — o que levaria horas no CustomTkinter leva minutos aqui
- **Visual profissional** — o layout já vem bonito sem configurar nada
- **Deploy gratuito** — em 5 minutos seu app tem uma URL pública na internet
- **Só Python** — sem HTML, sem CSS, sem JavaScript obrigatório
- **Câmera, upload de arquivo, slider, gráfico** — tudo pronto pra usar

### As limitações — e por que é importante saber disso

Aqui a gente vai ser honesto, porque ninguém merece descobrir as limitações de uma ferramenta no meio de um projeto importante.

> 🚧 **Limitação 1 — Streamlit reroda o script inteiro a cada interação**
>
> Toda vez que o usuário clica em um botão ou muda um input, o Python roda o arquivo do zero. Isso é diferente de tudo que vocês viram antes. Pode gerar bugs confusos no início, como variáveis que "resetam" do nada. A solução é o `session_state`, que veremos no Bloco 2. Vale a pena entender isso antes de ficar com raiva do Streamlit achando que é bug.

> 🚧 **Limitação 2 — Não é pra fazer qualquer tipo de site**
>
> Streamlit é ótimo pra ferramentas e apps internos. Mas não dá pra fazer um site institucional, uma loja virtual, um sistema com login complexo ou uma interface totalmente personalizada. Se um dia vocês precisarem disso, aí entram outras ferramentas — que a gente menciona logo abaixo.

> 🚧 **Limitação 3 — Performance com muitos usuários simultâneos**
>
> Se 500 pessoas abrirem seu app ao mesmo tempo, pode ficar lento. Isso não é problema pra projetos de portfólio ou ferramentas internas de equipes pequenas, mas é algo que uma empresa grande precisaria resolver com arquitetura diferente.

### O caminho depois do Streamlit

| Ferramenta | Quando usar | Dificuldade |
|---|---|---|
| **Streamlit ← vocês estão aqui** | Ferramentas rápidas, portfólio, protótipos com IA | ⭐ Iniciante |
| Flask | Sites simples, APIs, sistemas com rotas personalizadas | ⭐⭐ Intermediário |
| FastAPI | APIs profissionais, back-end de apps, integração com front-end | ⭐⭐⭐ Avançado |
| Django | Sistemas completos com banco de dados, login, painel admin | ⭐⭐⭐ Avançado |

Por hoje, foco total no Streamlit. Mas é bom vocês saberem que existe esse caminho — e que cada ferramenta faz sentido no seu momento.

---

## Antes de Começar

### Instalação
```bash
pip install streamlit
```

### Como rodar um app Streamlit
```bash
streamlit run meu_app.py
```

O Streamlit abre automaticamente no navegador. Cada vez que você salva o arquivo, a página recarrega sozinha.

### Código mínimo de referência (sempre visível na lousa)
```python
import streamlit as st

st.title("Meu Primeiro App")
st.write("Olá, turma!")
```

> 💡 **Dica para o professor:** Mantenha esse código base colado no quadro/projetor o tempo todo. Os alunos voltarão a ele constantemente. Salve o arquivo e mostre o navegador atualizando ao vivo — isso impressiona na primeira vez.

---

## BLOCO 1 — O que é Streamlit? Primeiros Widgets (1h)

### Objetivo
O aluno consegue criar um app com título, texto, imagem e pelo menos um input. Entende que cada arquivo `.py` é um app completo.

### 1.1 Por que Streamlit?

> *"Com CustomTkinter, a gente passava horas ajustando grid e pack. Com Streamlit, escrevemos Python puro e o navegador cuida do visual."*

Mostre ao vivo: abra o código mínimo, rode, mostre o navegador. Depois adicione uma linha. Salve. A página atualiza. Os alunos ficam impressionados com isso.

### 1.2 Widgets de Exibição

*Mostre cada widget com um exemplo ao vivo. Cole o código, rode, mostre o resultado.*

---

#### Widget 1 — `st.title()` e `st.write()`
```python
import streamlit as st

st.title("🐍 Meu App Python")
st.write("Esse texto aparece embaixo do título.")
st.write("Você pode passar qualquer coisa aqui: texto, números, dicionários...")
```

---

#### Widget 2 — `st.markdown()`
```python
import streamlit as st

st.title("Formatação com Markdown")
st.markdown("**Negrito**, *itálico*, e até listas:")
st.markdown("""
- Item um
- Item dois
- Item três
""")
```

> 💡 `st.markdown()` é muito útil para exibir respostas de IA, que geralmente vêm formatadas em markdown.

---

#### Widget 3 — `st.image()`
```python
import streamlit as st

# Imagem de uma URL da internet
st.image("https://picsum.photos/400/200", caption="Imagem aleatória da internet")

# Imagem local (arquivo na mesma pasta)
# st.image("foto.png", caption="Minha foto")
```

---

#### Widget 4 — `st.success()`, `st.error()`, `st.warning()`, `st.info()`
```python
import streamlit as st

st.success("✅ Operação concluída com sucesso!")
st.error("❌ Algo deu errado.")
st.warning("⚠️ Atenção: verifique os dados.")
st.info("ℹ️ Dica: você pode usar markdown aqui também.")
```

> 💡 Esses widgets substituem os `messagebox` do CTk. São perfeitos para feedback de API calls.

---

#### Widget 5 — `st.metric()`
```python
import streamlit as st

st.metric(label="Temperatura", value="28°C", delta="+3°C")
st.metric(label="Nota da Comida", value="8.5/10", delta="-0.5")
```

Ideal para exibir resultados de forma visual — temperatura de praia, nota de comida, preço de ação...

---

#### Widget 6 — `st.columns()`
```python
import streamlit as st

col1, col2, col3 = st.columns(3)

col1.metric("Temperatura", "28°C")
col2.metric("Chuva", "0mm")
col3.metric("Vento", "15 km/h")
```

> 💡 `st.columns()` é o substituto do `grid` do CTk. Muito mais simples e visual.

---

### 🎯 Mini-Desafio 1A — Cartão de Apresentação *(~10 min)*

> Crie um app com:
> - Um `st.title()` com seu nome
> - Um `st.write()` com uma frase sobre você
> - Um `st.success()` com seu hobbie favorito
> - Pelo menos 2 colunas com `st.columns()`
>
> ✅ Critério: o app roda no navegador sem erro.

---

## BLOCO 2 — Interatividade: Botões, Inputs e Lógica (1h)

### Objetivo
O aluno cria apps que reagem ao usuário: lê inputs, processa dados ao clicar em botão, e entende o conceito de `session_state`.

### 2.1 Widgets de Input

#### `st.text_input()` — campo de texto curto
```python
import streamlit as st

nome = st.text_input("Qual é o seu nome?", placeholder="Ex: Maria Silva")
st.write(f"Olá, {nome}!")
```

> ⚠️ **Atenção:** O Streamlit reroda o script inteiro a cada interação. Isso é diferente do CTk. Por enquanto, aceite como comportamento normal. Explicaremos o `session_state` logo.

---

#### `st.text_area()` — campo de texto longo
```python
import streamlit as st

curriculo = st.text_area("Cole o seu currículo aqui:", height=200,
                          placeholder="Copie e cole seu currículo...")
st.write(f"Seu currículo tem {len(curriculo)} caracteres.")
```

---

#### `st.selectbox()` — menu dropdown
```python
import streamlit as st

area = st.selectbox(
    "Qual área te interessa?",
    ["Tecnologia", "Administração", "Finanças", "Saúde", "Educação"]
)
st.write(f"Você escolheu: {area}")
```

---

#### `st.slider()` — controle deslizante
```python
import streamlit as st

nivel = st.slider("Nível de experiência (1-10):", min_value=1, max_value=10, value=5)
st.write(f"Nível: {nivel}/10")
```

---

#### `st.file_uploader()` — upload de arquivo
```python
import streamlit as st

arquivo = st.file_uploader("Faça upload de uma imagem:", type=["png", "jpg", "jpeg"])
if arquivo is not None:
    st.image(arquivo, caption="Sua imagem", width=300)
```

---

#### `st.camera_input()` — câmera do dispositivo
```python
import streamlit as st

foto = st.camera_input("Tire uma foto da sua comida:")
if foto is not None:
    st.image(foto, caption="Foto capturada!", width=300)
    st.success("Foto recebida! Pronto para analisar.")
```

> 💡 `st.camera_input()` é ouro para o projeto FoodGrader. Funciona no celular também quando o app está no Streamlit Cloud.

---

### 2.2 `st.button()` e a lógica do app
```python
import streamlit as st

nome = st.text_input("Seu nome:")

if st.button("Gerar saudação"):
    if nome:
        st.success(f"Olá, {nome}! Seja bem-vindo(a)!")
    else:
        st.error("Por favor, digite seu nome primeiro.")
```

> *"O botão retorna `True` quando clicado. Por isso usamos `if st.button()`. Tudo dentro do `if` só executa quando o usuário clica."*

---

### 2.3 `st.spinner()` — feedback durante processamento
```python
import streamlit as st
import time

if st.button("Processar (demora 2 segundos)"):
    with st.spinner("Processando... aguarde..."):
        time.sleep(2)  # simula uma API call
    st.success("Processamento concluído!")
```

> 💡 `st.spinner()` é essencial para chamadas de API. O usuário vê uma animação enquanto a IA responde. Sem isso, parece que o app travou.

---

### 2.4 `st.session_state` — memória entre interações

> *"O Streamlit reroda o script inteiro a cada clique. Se você quer lembrar alguma coisa entre um clique e outro, usa `session_state`."*

```python
import streamlit as st

# Inicializa o contador na primeira vez
if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("Clique aqui"):
    st.session_state.contador += 1

st.write(f"Você clicou {st.session_state.contador} vezes")
```

No contexto dos nossos projetos, usaremos `session_state` para guardar a resposta da IA entre reruns.

---

### 🎯 Mini-Desafio 2A — Churrascômetro *(~15 min)*

> Crie um app que calcula quanto comprar para um churrasco.
>
> **Inputs:**
> - Número de adultos (`st.number_input`)
> - Número de crianças (`st.number_input`)
>
> **Mostre as fórmulas antes do botão** (use `st.info()` ou `st.markdown()`):
> - 🥩 Carne: 300g por adulto / 150g por criança
> - 🥤 Bebidas: 1,5L por adulto / 0,75L por criança
> - 🥗 Acompanhamentos: 200g por pessoa (adulto e criança)
>
> **Botão:** "Calcular Churrasco"
>
> **Resultados com `st.metric()`:**
> - Carne total (kg)
> - Bebidas totais (L)
> - Acompanhamentos (kg)
>
> ✅ Critério: os três `st.metric()` exibem os valores corretos ao clicar no botão.

---

## BLOCO 3 — Conectando com APIs Externas (1h30)

### Objetivo
O aluno faz uma chamada real a uma API (clima ou IA), exibe o resultado no app, e entende o fluxo input → API → output.

### 3.1 O fluxo de todo app com API

> *"Todo app com API segue o mesmo padrão, não importa se é clima, IA, câmbio ou qualquer outra coisa."*

```python
# PADRÃO UNIVERSAL DE APP COM API:
#
# 1. Pegar input do usuário (st.text_input, st.file_uploader...)
# 2. Usuário clica no botão
# 3. Mostrar st.spinner()
# 4. Fazer a chamada para a API (requests, biblioteca específica...)
# 5. Receber e processar a resposta
# 6. Exibir o resultado para o usuário
```

---

### 3.2 Exemplo: ViaCEP — API sem autenticação *(aquecimento)*

Antes de APIs com chave e cadastro, vamos usar uma API brasileira, gratuita e sem nenhuma autenticação: o **ViaCEP**. Só precisamos mandar um CEP e ela devolve o endereço completo.

> *"Toda API funciona assim: você manda uma URL com os dados que quer, ela devolve um JSON com a resposta."*

**URL do ViaCEP:**
```
https://viacep.com.br/ws/{CEP}/json/
```

**JSON que ela devolve (estrutura plana — fácil de ler):**
```json
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP"
}
```

**Código completo — Buscador de CEP:**
```python
import streamlit as st
import requests

st.title("📮 Buscador de CEP")

# st.text_input retorna uma string com o que o usuário digitou
cep = st.text_input("Digite o CEP:", placeholder="Ex: 01001-000")

if st.button("Buscar Endereço"):
    if not cep:
        st.error("Digite um CEP primeiro!")
    else:
        # Removemos traços e espaços — a API só aceita números
        cep_limpo = cep.replace("-", "").replace(" ", "")

        with st.spinner("Buscando endereço..."):
            url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
            resposta = requests.get(url)  # GET simples, sem chave, sem headers
            dados = resposta.json()       # converte o JSON em dicionário Python

        # A API retorna {"erro": true} se o CEP não existir
        if "erro" in dados:
            st.error("CEP não encontrado. Verifique os números.")
        else:
            # Lendo as chaves do dicionário — igual a qualquer dict em Python
            st.success("Endereço encontrado!")
            col1, col2 = st.columns(2)
            col1.metric("Cidade", dados["localidade"])
            col2.metric("Estado", dados["uf"])
            st.write(f"**Logradouro:** {dados['logradouro']}")
            st.write(f"**Bairro:** {dados['bairro']}")
```

> 💡 **Como explorar em aula:** Mostre o JSON bruto primeiro — abra `https://viacep.com.br/ws/01001000/json/` no navegador. Os alunos veem o dicionário "ao vivo" antes de qualquer código. Peça que cada um busque o CEP da própria casa.

---

### 🎯 Exercício Guiado 3B — Buscador de Países (RestCountries)

#### Por que esse exercício?

O ViaCEP foi um aquecimento: JSON simples, resposta direto no dicionário, campos fáceis de ler. Agora vamos subir um degrau. A RestCountries devolve uma **lista**, as informações ficam em **dicionários aninhados**, e campos como idiomas e moedas precisam de um loop para ler. É exatamente o tipo de JSON que vocês vão encontrar em APIs reais.

E de propósito, vamos fazer em **duas etapas**: primeiro só Python no terminal, sem nenhuma interface. Só quando os dados estiverem aparecendo certinhos no terminal é que a gente adiciona o Streamlit por cima.

> 🧠 **Por que essa ordem importa?** Misturar extração de dados com interface ao mesmo tempo dobra o número de coisas que podem dar errado. Separar as etapas facilita encontrar o problema quando algo não funciona.

---

#### A API que vamos usar

**URL:**
```
https://restcountries.com/v3.1/name/{nome_do_pais}
```

Sem cadastro, sem chave, sem header. Só GET.

**Abra no navegador antes de qualquer código:**
```
https://restcountries.com/v3.1/name/brazil
```

Observe com atenção:
- A resposta começa com `[` — é uma **lista**, não um dicionário direto
- Dentro da lista existe um dicionário `{}` com as informações do país
- Campos como `languages` e `currencies` são dicionários dentro do dicionário
- O campo `capital` é uma **lista** (um país pode ter mais de uma capital)
- O campo `translations` tem o nome do país em vários idiomas, incluindo `"por"` (português)

---

#### Etapa 1 — Extrair os dados no terminal (sem Streamlit)

*Crie um arquivo `busca_pais.py`. Construa junto com os alunos, um bloco por vez.*

---

**Bloco 1 — Fazer a chamada e ver o que chega**

```python
import requests

pais = "brazil"
url = f"https://restcountries.com/v3.1/name/{pais}"

resposta = requests.get(url)
dados = resposta.json()

print(type(dados))   # vamos ver que tipo de objeto chegou
print(len(dados))    # quantos resultados vieram?
```

Rode. O terminal vai mostrar `<class 'list'>` e `1`. Explique: a API sempre devolve uma lista, mesmo quando só encontra um país. Isso é porque uma busca por "guinea" pode retornar vários países (Guinea, Papua Nova Guiné, etc.).

---

**Bloco 2 — Entrar no primeiro item da lista**

```python
# dados é uma lista — pegamos o primeiro item com [0]
pais_info = dados[0]

# Isso imprime todas as chaves disponíveis nesse dicionário
for chave in pais_info.keys():
    print(chave)
```

Rode. Mostre a lista de chaves. Pergunte aos alunos: "qual chave tem o nome em português?" Eles vão apontar para `translations`.

---

**Bloco 3 — Extrair os campos simples**

```python
# Nome oficial em português — está dentro de translations > por > official
nome_pt = pais_info["translations"]["por"]["official"]

# População — número direto
populacao = pais_info["population"]

# Capital — é uma lista, pegamos a primeira posição
capital = pais_info["capital"][0]

print(f"Nome oficial (PT): {nome_pt}")
print(f"População: {populacao}")
print(f"Capital: {capital}")
```

Rode. Os três campos aparecem. Pause aqui e pergunte: "por que `capital[0]` e não só `capital`?" Deixe alguém responder — um país pode ter mais de uma capital.

---

**Bloco 4 — Extrair idiomas (dicionário → loop)**

```python
# languages é um dicionário: {"por": "Portuguese", "eng": "English", ...}
# Queremos só os nomes, não os códigos
idiomas = pais_info["languages"]

print("Idiomas:")
for codigo, nome in idiomas.items():
    print(f"  - {nome}")
```

Rode. Explique: `.items()` devolve pares `(chave, valor)`. O código do idioma (ex: `"por"`) vai para `codigo`, o nome vai para `nome`. Nesse exercício, só precisamos do nome.

---

**Bloco 5 — Extrair moeda (dicionário de dicionários → loop)**

```python
# currencies é um dicionário de dicionários:
# {"BRL": {"name": "Brazilian real", "symbol": "R$"}}
moedas = pais_info["currencies"]

print("Moedas:")
for codigo, info in moedas.items():
    print(f"  - {info['name']} ({info['symbol']})")
```

Rode. Explique que `info` aqui é um dicionário com `name` e `symbol`. Usamos `info['name']` para pegar o nome.

---

**Bloco 6 — Pegar a bandeira**

```python
# flags tem as URLs das imagens da bandeira
bandeira_url = pais_info["flags"]["png"]

print(f"Bandeira: {bandeira_url}")
```

Cole a URL no navegador. A bandeira aparece. Vai ser usada como imagem no Streamlit.

---

**Código completo da Etapa 1** *(para referência — não cole direto, construa junto)*

```python
import requests

pais = "brazil"
url = f"https://restcountries.com/v3.1/name/{pais}"

resposta = requests.get(url)
dados = resposta.json()
pais_info = dados[0]

# Campos simples
nome_pt  = pais_info["translations"]["por"]["official"]
populacao = pais_info["population"]
capital  = pais_info["capital"][0]
bandeira = pais_info["flags"]["png"]

# Idiomas — monta uma string "Português, Inglês"
lista_idiomas = []
for codigo, nome in pais_info["languages"].items():
    lista_idiomas.append(nome)
idiomas_str = ", ".join(lista_idiomas)

# Moedas — monta uma string "Real Brasileiro (R$)"
lista_moedas = []
for codigo, info in pais_info["currencies"].items():
    lista_moedas.append(f"{info['name']} ({info['symbol']})")
moedas_str = ", ".join(lista_moedas)

# Exibe tudo
print(f"Nome oficial: {nome_pt}")
print(f"Capital:      {capital}")
print(f"População:    {populacao:,}")
print(f"Idiomas:      {idiomas_str}")
print(f"Moeda:        {moedas_str}")
print(f"Bandeira:     {bandeira}")
```

> 💡 **Como explorar em aula:** Depois de rodar com "brazil", peçam que cada aluno tente o país de origem da família, ou um país favorito. Erros de digitação são bem-vindos — a API vai retornar status 404, que a gente trata na Etapa 2.

---

#### Etapa 2 — Adicionar a interface Streamlit

Agora que os dados estão saindo certinho no terminal, a gente só precisa:
1. Trocar o `pais = "brazil"` fixo por um `st.text_input`
2. Envolver a chamada com um `st.button` e um `st.spinner`
3. Trocar os `print()` por widgets do Streamlit

*Crie um arquivo `app_paises.py`.*

---

**Passo 1 — Estrutura básica com input e botão**

```python
import streamlit as st
import requests

st.title("🌍 Buscador de Países")
st.write("Digite o nome de um país em inglês para ver suas informações.")

nome = st.text_input("Nome do país:", placeholder="Ex: brazil, france, japan")

if st.button("Buscar"):
    if not nome:
        st.error("Digite o nome de um país primeiro!")
```

Rode. Mostre o input e o botão funcionando. A mensagem de erro aparece se o botão for clicado com o campo vazio.

---

**Passo 2 — Chamar a API e tratar o caso de país não encontrado**

```python
import streamlit as st
import requests

st.title("🌍 Buscador de Países")
st.write("Digite o nome de um país em inglês para ver suas informações.")

nome = st.text_input("Nome do país:", placeholder="Ex: brazil, france, japan")

if st.button("Buscar"):
    if not nome:
        st.error("Digite o nome de um país primeiro!")
    else:
        url = f"https://restcountries.com/v3.1/name/{nome}"

        with st.spinner("Buscando informações..."):
            resposta = requests.get(url)

        if resposta.status_code == 404:
            st.error(f"País '{nome}' não encontrado. Verifique o nome.")
        else:
            dados = resposta.json()
            pais_info = dados[0]
            st.success("País encontrado!")
            st.write(pais_info)  # mostra o dicionário bruto por enquanto
```

Rode. Teste com "brazil" e com um nome errado como "brazill". Mostre que o dicionário bruto aparece na tela — feio, mas funcionando. Explique que o próximo passo é substituir o `st.write(pais_info)` pelos widgets certos.

---

**Passo 3 — Exibir os dados com visual**

Substitua o `st.write(pais_info)` pelo bloco abaixo:

```python
            # Extração dos dados — igual ao que fizemos no terminal
            nome_pt   = pais_info["translations"]["por"]["official"]
            populacao = pais_info["population"]
            capital   = pais_info["capital"][0]
            bandeira  = pais_info["flags"]["png"]

            lista_idiomas = []
            for codigo, idioma in pais_info["languages"].items():
                lista_idiomas.append(idioma)
            idiomas_str = ", ".join(lista_idiomas)

            lista_moedas = []
            for codigo, info in pais_info["currencies"].items():
                lista_moedas.append(f"{info['name']} ({info['symbol']})")
            moedas_str = ", ".join(lista_moedas)

            # Exibição com Streamlit
            st.divider()

            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(bandeira, width=180)

            with col2:
                st.subheader(nome_pt)
                st.metric("Capital", capital)
                st.metric("População", f"{populacao:,}")

            st.divider()

            st.write(f"**Idiomas:** {idiomas_str}")
            st.write(f"**Moeda:** {moedas_str}")
```

Rode com "brazil". A bandeira e os dados aparecem lado a lado.

> 💡 `st.columns([1, 2])` cria duas colunas com proporções diferentes — a segunda é o dobro da primeira. Ótimo para colocar imagem ao lado de texto.

---

**Código completo — `app_paises.py`**

```python
import streamlit as st
import requests

st.title("🌍 Buscador de Países")
st.write("Digite o nome de um país em inglês para ver suas informações.")

nome = st.text_input("Nome do país:", placeholder="Ex: brazil, france, japan")

if st.button("Buscar"):
    if not nome:
        st.error("Digite o nome de um país primeiro!")
    else:
        url = f"https://restcountries.com/v3.1/name/{nome}"

        with st.spinner("Buscando informações..."):
            resposta = requests.get(url)

        if resposta.status_code == 404:
            st.error(f"País '{nome}' não encontrado. Verifique o nome em inglês.")
        else:
            dados = resposta.json()
            pais_info = dados[0]

            # Extração
            nome_pt   = pais_info["translations"]["por"]["official"]
            populacao = pais_info["population"]
            capital   = pais_info["capital"][0]
            bandeira  = pais_info["flags"]["png"]

            lista_idiomas = []
            for codigo, idioma in pais_info["languages"].items():
                lista_idiomas.append(idioma)
            idiomas_str = ", ".join(lista_idiomas)

            lista_moedas = []
            for codigo, info in pais_info["currencies"].items():
                lista_moedas.append(f"{info['name']} ({info['symbol']})")
            moedas_str = ", ".join(lista_moedas)

            # Exibição
            st.divider()

            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(bandeira, width=180)

            with col2:
                st.subheader(nome_pt)
                st.metric("Capital", capital)
                st.metric("População", f"{populacao:,}")

            st.divider()

            st.write(f"**Idiomas:** {idiomas_str}")
            st.write(f"**Moeda:** {moedas_str}")
```

> 💡 **Como explorar em aula:** Peça que cada aluno busque um país diferente. Depois teste "guinea" — vai retornar a Guiné mas não a Papua Nova Guiné (que seria `papua new guinea`). Ótima discussão sobre como APIs devolvem múltiplos resultados e `dados[0]` pega só o primeiro.

---

### 🎯 Mini-Desafio 3B — Comparador de Países *(~15 min)*

> A partir do app de países que vocês acabaram de construir, adicione:
> - Um **segundo campo** `st.text_input` para um segundo país
> - Exiba as informações dos dois países **lado a lado** com `st.columns(2)`
> - Se um país não for encontrado mas o outro sim, mostre o erro só para o que falhou
>
> ✅ Critério: os dois países aparecem lado a lado sem que um erro quebre o outro.

---

### 3.3 Exemplo: API de Clima (OpenWeatherMap)

A API de clima é gratuita e tem cadastro simples. Perfeita para o projeto "Praia sem Chuva".

**Instalação:**
```bash
pip install requests
```

**Código completo — Consulta de Clima:**
```python
import streamlit as st
import requests

API_KEY = "sua_chave_aqui"  # cadastro grátis em openweathermap.org

st.title("🌤️ Consultor de Clima")

cidade = st.text_input("Digite o nome da cidade:", placeholder="Ex: Santos, BR")

if st.button("Ver Clima"):
    if not cidade:
        st.error("Digite uma cidade primeiro!")
    else:
        with st.spinner(f"Buscando clima em {cidade}..."):
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": cidade,
                "appid": API_KEY,
                "units": "metric",
                "lang": "pt_br"
            }
            resposta = requests.get(url, params=params)
            dados = resposta.json()

        if resposta.status_code == 200:
            temp    = dados["main"]["temp"]
            descr   = dados["weather"][0]["description"]
            chuva   = dados.get("rain", {}).get("1h", 0)
            umidade = dados["main"]["humidity"]

            col1, col2 = st.columns(2)
            col1.metric("Temperatura", f"{temp:.1f}°C")
            col2.metric("Umidade", f"{umidade}%")

            st.write(f"**Condição:** {descr.capitalize()}")

            if chuva == 0:
                st.success("✅ Sem chuva! Boa hora para ir à praia.")
            else:
                st.error(f"🌧️ Chovendo {chuva}mm/h. Fique em casa.")
        else:
            st.error("Cidade não encontrada. Verifique o nome.")
```

> 💡 Mostre ao vivo: teste Santos, Florianópolis, Rio de Janeiro. Deixe os alunos digitarem suas cidades natais — cria engajamento imediato. Explique cada chave do JSON conforme vai lendo (`dados["main"]["temp"]` etc.)

---

### 3.3 Exemplo: API de IA (Anthropic / Claude)

Esse padrão se repete para qualquer IA — OpenAI, Gemini, Claude. Quem aprende um, aprende todos.

**Instalação:**
```bash
pip install anthropic
```

**Código completo — Gerador de Texto com IA:**
```python
import streamlit as st
import anthropic

st.title("🤖 Gerador de Texto com IA")

tema = st.text_input("Sobre o que você quer que a IA escreva?",
                      placeholder="Ex: os benefícios da leitura")
estilo = st.selectbox("Estilo:", ["Formal", "Descontraído", "Técnico", "Poético"])

if st.button("Gerar com IA"):
    if not tema:
        st.error("Digite um tema primeiro!")
    else:
        with st.spinner("A IA está escrevendo..."):
            client = anthropic.Anthropic(api_key="sua_chave_aqui")
            mensagem = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=500,
                messages=[{
                    "role": "user",
                    "content": f"Escreva um parágrafo sobre '{tema}' no estilo {estilo}."
                }]
            )
            resposta = mensagem.content[0].text

        st.markdown("### Resposta da IA:")
        st.markdown(resposta)
        st.success("Texto gerado com sucesso!")
```

> ⚠️ **Atenção:** Nunca coloque sua API key diretamente no código se for publicar. Use `st.secrets` ou variáveis de ambiente. Para a aula, chave no código é aceitável para testar localmente.

---

### 3.4 Gerenciando a API Key com `st.secrets`

```toml
# Crie o arquivo .streamlit/secrets.toml na pasta do projeto:
ANTHROPIC_KEY = "sua_chave_aqui"
WEATHER_KEY   = "sua_chave_aqui"
```

```python
# No seu código Python:
import streamlit as st

client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_KEY"])
```

> 💡 No Streamlit Cloud, você configura os secrets pelo painel web. Nunca vão para o GitHub.

---

### 🎯 Mini-Desafio 3A — App de Piada *(~20 min)*

> Crie um app que:
> - Tem um `selectbox` com categorias: "Tecnologia", "Escola", "Esportes", "Animais"
> - Tem um botão "Contar Piada"
> - Chama a IA pedindo uma piada da categoria escolhida
> - Exibe a piada com `st.markdown()`
> - Mostra `st.spinner()` enquanto a IA responde
>
> **Bônus:** adicionar um botão "Nova Piada" que gera outra sem recarregar a página
>
> ✅ Critério: a piada gerada muda conforme a categoria selecionada.

---

## BLOCO 4 — Projeto Guiado: FoodGrader com IA (1h30)

### Objetivo
O aluno constrói do zero um app completo de análise de comida com câmera e IA, aplicando todos os conceitos anteriores.

### 4.1 Visão geral do projeto

O FoodGrader tira uma foto da comida (ou faz upload de imagem), envia para a IA, e recebe uma análise nutricional com nota.

| Funcionalidade | Widget/Recurso |
|---|---|
| Capturar foto | `st.camera_input()` |
| Upload de imagem | `st.file_uploader()` |
| Enviar imagem para IA | Anthropic API (visão) |
| Exibir nota | `st.metric()` |
| Exibir análise | `st.markdown()` |
| Feedback visual | `st.success()` / `st.warning()` |

---

### 4.2 Passo a passo — construção ao vivo

*Construa junto com os alunos. Um passo por vez, testando a cada adição.*

#### Passo 1 — Estrutura básica e título
```python
import streamlit as st
import anthropic
import base64

st.title("🍔 FoodGrader")
st.markdown("Tire uma foto da sua comida e receba uma análise nutricional com IA!")
```

---

#### Passo 2 — Input de imagem (câmera ou upload)
```python
# ... (código anterior)

st.markdown("---")
opcao = st.radio("Como você quer enviar a imagem?",
                  ["📷 Câmera", "📁 Upload de arquivo"])

imagem = None

if opcao == "📷 Câmera":
    imagem = st.camera_input("Aponte para o prato:")
else:
    imagem = st.file_uploader("Escolha uma foto da comida:",
                               type=["png", "jpg", "jpeg"])

if imagem:
    st.image(imagem, caption="Imagem recebida!", width=350)
```

---

#### Passo 3 — Botão de análise e chamada para a IA
```python
# ... (código anterior)

if imagem:
    st.image(imagem, caption="Imagem recebida!", width=350)

    if st.button("🔍 Analisar com IA"):
        with st.spinner("A IA está analisando sua comida..."):

            # Converte a imagem para base64 (formato que a IA aceita)
            bytes_imagem = imagem.getvalue()
            base64_imagem = base64.b64encode(bytes_imagem).decode("utf-8")

            client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_KEY"])

            mensagem = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=600,
                messages=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": base64_imagem
                            }
                        },
                        {
                            "type": "text",
                            "text": """Analise essa comida e retorne EXATAMENTE neste formato:
NOTA: [número de 1 a 10]
CALORIAS: [estimativa]
PROTEINAS: [estimativa em gramas]
CARBOIDRATOS: [estimativa em gramas]
AVALIACAO: [2-3 frases sobre a qualidade nutricional]
SUGESTAO: [1 sugestão para melhorar o prato]"""
                        }
                    ]
                }]
            )

            st.session_state.resultado = mensagem.content[0].text
```

---

#### Passo 4 — Exibir resultado de forma elegante
```python
# ... (após receber o resultado da IA)

if "resultado" in st.session_state:
    resultado = st.session_state.resultado
    linhas = {}
    for linha in resultado.split("\n"):
        if ":" in linha:
            chave, valor = linha.split(":", 1)
            linhas[chave.strip()] = valor.strip()

    st.markdown("---")
    st.markdown("### 📊 Resultado da Análise")

    nota_texto = linhas.get("NOTA", "?")
    try:
        nota = float(nota_texto)
        col1, col2, col3 = st.columns(3)
        col1.metric("Nota", f"{nota}/10")
        col2.metric("Calorias (est.)", linhas.get("CALORIAS", "—"))
        col3.metric("Proteínas", linhas.get("PROTEINAS", "—"))

        if nota >= 7:
            st.success("✅ Prato saudável! Continue assim.")
        elif nota >= 5:
            st.warning("⚠️ Prato moderado. Veja a sugestão abaixo.")
        else:
            st.error("❌ Prato pouco nutritivo. Considere alternativas.")
    except:
        pass

    if "AVALIACAO" in linhas:
        st.markdown(f"**Avaliação:** {linhas['AVALIACAO']}")
    if "SUGESTAO" in linhas:
        st.info(f"💡 Sugestão: {linhas['SUGESTAO']}")
```

> 💡 Faça ao vivo com comida de verdade se possível — pizza, fruta, marmita. O contraste entre uma salada (nota alta) e uma batata frita (nota baixa) é didático. Se não tiver câmera, use `st.file_uploader` com imagens baixadas da internet.

---

### 4.3 Código completo do FoodGrader

```python
import streamlit as st
import anthropic
import base64

st.set_page_config(page_title="FoodGrader", page_icon="🍔", layout="centered")
st.title("🍔 FoodGrader")
st.markdown("Analise sua comida com Inteligência Artificial!")

opcao = st.radio("Como enviar a imagem?", ["📷 Câmera", "📁 Upload"])
imagem = st.camera_input("Foto:") if opcao == "📷 Câmera" else st.file_uploader("Arquivo:", type=["png","jpg","jpeg"])

if imagem:
    st.image(imagem, width=350)

    if st.button("🔍 Analisar"):
        with st.spinner("Analisando..."):
            img_b64 = base64.b64encode(imagem.getvalue()).decode()
            client  = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_KEY"])
            msg     = client.messages.create(
                model="claude-opus-4-5", max_tokens=600,
                messages=[{"role":"user","content":[
                    {"type":"image","source":{"type":"base64","media_type":"image/jpeg","data":img_b64}},
                    {"type":"text","text":"Analise essa comida. Responda EXATAMENTE:\nNOTA: [1-10]\nCALORIAS: [estimativa]\nPROTEINAS: [g]\nAVALIACAO: [2 frases]\nSUGESTAO: [1 sugestão]"}
                ]}]
            )
            st.session_state.res = msg.content[0].text

if "res" in st.session_state:
    linhas = {}
    for l in st.session_state.res.split("\n"):
        if ":" in l:
            k, v = l.split(":", 1)
            linhas[k.strip()] = v.strip()
    st.markdown("---")
    nota = float(linhas.get("NOTA", "5"))
    col1, col2 = st.columns(2)
    col1.metric("Nota", f"{nota:.1f}/10")
    col2.metric("Calorias", linhas.get("CALORIAS", "—"))
    ([st.success, st.warning, st.error][0 if nota >= 7 else 1 if nota >= 5 else 2])(
        linhas.get("AVALIACAO", ""))
    if "SUGESTAO" in linhas:
        st.info(f"💡 {linhas['SUGESTAO']}")
```

---

### 🎯 Desafio 4A — Expandir o FoodGrader *(~20 min)*

> Adicione ao FoodGrader:
> - Um histórico de análises usando `st.session_state` (lista de resultados anteriores)
> - Um botão "Ver Histórico" que mostra os últimos 3 pratos analisados
> - Um `st.selectbox` para escolher o idioma da análise (Português / Inglês / Espanhol)
>
> **Bônus:** adicionar `st.download_button` para baixar o resultado como `.txt`
>
> ✅ Critério: o histórico persiste entre análises sem perder os dados anteriores.

---

## BLOCO 5 — Desafios Progressivos e Deploy Gratuito (1h)

### Objetivo
O aluno publica seu app na internet gratuitamente e inicia desafios de projeto com as APIs vistas ao longo do curso.

### 5.1 Deploy no Streamlit Cloud — passo a passo

> *"Tudo que fizemos roda local. Agora vamos publicar na internet de graça, em 5 minutos."*

**Passo 1 — Estrutura de pastas do projeto:**
```
meu_app/
├── app.py              ← código principal
├── requirements.txt    ← bibliotecas necessárias
└── .streamlit/
    └── secrets.toml    ← chaves de API (NÃO vai para o GitHub!)
```

**Passo 2 — `requirements.txt`:**
```
streamlit
anthropic
requests
```

**Passo 3 — Publicar:**
```
1. Crie uma conta gratuita em github.com
2. Crie um repositório novo e envie o projeto
   (sem o arquivo secrets.toml!)
3. Acesse share.streamlit.io
4. Conecte com o GitHub, escolha o repositório
5. Configure as secrets no painel do Streamlit Cloud
6. Clique em Deploy
7. Em ~2 minutos, seu app tem uma URL pública!
```

> 💡 O arquivo `secrets.toml` NUNCA vai para o GitHub. Configure as secrets pelo painel web do Streamlit Cloud. A URL gerada é pública — qualquer pessoa com o link acessa o app. Excelente para colocar no portfólio e mostrar em entrevistas.

---

### 5.2 Desafios Progressivos de Projeto

*Instrução para o professor: os alunos escolhem UM projeto e desenvolvem pelo tempo restante. Você circula e apoia.*

---

### 🎯 Nível 1 — CV Tailor Bot

> App que recebe um currículo e uma vaga de emprego e reescreve o currículo para a vaga.
>
> **Widgets:** `st.text_area` (currículo), `st.text_area` (descrição da vaga), `st.button`, `st.markdown`
>
> **API:** IA para reescrever o currículo
>
> **Prompt sugerido:**
> *"Você é um especialista em RH. Dado este currículo e esta vaga, reescreva o currículo destacando as experiências mais relevantes para a vaga. Mantenha as informações verídicas."*
>
> ✅ Entrega: app funcional que gera um currículo adaptado para qualquer vaga colada.

---

### 🎯 Nível 2 — Praia sem Chuva

> App que compara o clima de várias praias e recomenda a melhor opção.
>
> **Widgets:** `st.multiselect` (lista de praias), `st.button`, `st.columns`, `st.metric`
>
> **APIs:** OpenWeatherMap (clima) + IA (para gerar recomendação em texto)
>
> **Fluxo:**
> 1. Usuário seleciona até 5 praias
> 2. App busca clima das 5 ao mesmo tempo
> 3. Exibe tabela comparativa (temp, chuva, vento)
> 4. IA gera parágrafo recomendando a melhor opção
>
> ✅ Entrega: app que compara praias e recomenda com justificativa da IA.

---

### 🎯 Nível 3 — App Livre (área de interesse)

> O aluno cria um app para sua área de interesse usando IA e pelo menos uma API externa.
>
> **Exemplos por área:**
> - Administração: gerador de e-mails profissionais, analisador de contratos
> - Finanças: calculadora de investimentos com projeção da IA
> - Saúde: diário de sintomas com análise da IA
> - Educação: criador de questões de prova, resumidor de textos
> - Esportes: analisador de desempenho físico
>
> **Requisitos mínimos:**
> - Pelo menos 1 API call (IA ou outra)
> - `st.spinner()` durante o processamento
> - Resultado exibido com pelo menos 3 tipos de widget diferentes
> - App publicado no Streamlit Cloud com URL pública
>
> ✅ Entrega: link do app publicado + 2 minutos explicando o que faz.

---

## Referência Rápida — Widgets Streamlit

| Widget | Para que serve | Retorna |
|---|---|---|
| `st.title(text)` | Título grande | — |
| `st.write(valor)` | Exibir qualquer valor | — |
| `st.markdown(text)` | Texto com formatação | — |
| `st.success/error/warning/info(text)` | Feedback colorido | — |
| `st.metric(label, value, delta)` | Indicador visual | — |
| `st.image(imagem)` | Exibir imagem | — |
| `st.text_input(label)` | Campo de texto curto | `str` |
| `st.text_area(label)` | Campo de texto longo | `str` |
| `st.number_input(label)` | Campo numérico | `int/float` |
| `st.selectbox(label, options)` | Menu dropdown | valor escolhido |
| `st.multiselect(label, options)` | Seleção múltipla | `list` |
| `st.slider(label, min, max)` | Controle deslizante | `int/float` |
| `st.radio(label, options)` | Botões de escolha | valor escolhido |
| `st.button(label)` | Botão clicável | `bool` |
| `st.file_uploader(label, type)` | Upload de arquivo | arquivo ou `None` |
| `st.camera_input(label)` | Câmera do dispositivo | foto ou `None` |
| `st.columns(n)` | Dividir em colunas | lista de colunas |
| `st.spinner(text)` | Animação de loading | context manager |
| `st.session_state` | Memória entre reruns | dict-like |

---

## Referência Rápida — Padrão de Chamada de API

```python
import streamlit as st

# PADRÃO PARA QUALQUER APP COM API:
entrada = st.text_input("Dado do usuário:")

if st.button("Processar"):
    if not entrada:
        st.error("Preencha o campo!")
    else:
        with st.spinner("Aguarde..."):
            resultado = chamar_api(entrada)   # substitua pela sua função
            st.session_state.resultado = resultado

if "resultado" in st.session_state:
    st.markdown(st.session_state.resultado)
```

---

## Referência Rápida — Estrutura de Projeto

```
meu_projeto/
├── app.py              ← código Streamlit
├── requirements.txt    ← streamlit, anthropic, requests...
└── .streamlit/
    └── secrets.toml    ← ANTHROPIC_KEY = "sk-ant-..."
                           (nunca subir para o GitHub!)
```

---

*Plano elaborado para turmas do ensino médio público — foco em apps com IA que impressionam em entrevistas.*
