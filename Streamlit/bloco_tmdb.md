## BLOCO 3.5 — HTTP Status Codes + TMDB: Primeira API Autenticada (1h30)

### Objetivo
O aluno entende os códigos de status HTTP mais comuns, sabe tratar cada um no código, faz sua primeira chamada a uma API que exige autenticação por header, usa `@st.cache_data` para não rebater o endpoint a cada rerun, e constrói uma interface com sidebar e layout em colunas.

---

### 3.5.1 Pausa para teoria — HTTP Status Codes (~10 min)

Até agora, quando fizemos chamadas de API, a gente mais ou menos confiou que ia dar certo. Quando não dava, o código quebrava ou a gente olhava o JSON e via um campo `"erro"`. Mas toda resposta HTTP — de qualquer API do mundo — traz junto um **número de três dígitos** que diz exatamente o que aconteceu.

> *"Esse número é o primeiro lugar pra olhar quando uma API não funciona. Antes de xingar o código, antes de ligar pro suporte, antes de chorar: leia o status code."*

#### A analogia do restaurante

Imagine que você entra num restaurante e faz um pedido. O garçom sempre responde, mas a resposta varia:

| Código | O que o garçom diz | O que significa |
|---|---|---|
| **200 OK** | "Aqui está seu prato!" | Deu certo, tá tudo lá |
| **400 Bad Request** | "Seu pedido tá ilegível, não entendi" | Você mandou dado errado |
| **401 Unauthorized** | "Você não fez reserva, não pode entrar" | Falta autenticação (chave errada ou ausente) |
| **403 Forbidden** | "Sei quem você é, mas você não pode pedir isso" | Autenticado, mas sem permissão |
| **404 Not Found** | "Esse prato não existe no cardápio" | O recurso não existe |
| **429 Too Many Requests** | "Calma, você já pediu 50 vezes em 1 minuto" | Bateu o limite de uso |
| **500 Internal Server Error** | "A cozinha pegou fogo, não é culpa sua" | A API está com problema interno |

#### A regra geral dos grupos

Não precisa decorar todos os códigos — só saber o que cada centena significa:

- **2xx → Sucesso.** Tudo ocorreu bem.
- **3xx → Redirecionamento.** "Esse conteúdo mudou de endereço." Raro de tratar à mão, o `requests` resolve sozinho.
- **4xx → Erro do cliente (você).** Você mandou algo errado: URL errada, chave errada, parâmetro faltando.
- **5xx → Erro do servidor (a API).** Não é culpa sua. Tenta de novo mais tarde.

> 💡 **Sacada pro professor:** Cole essa tabela no quadro e deixa visível o resto da aula. Toda vez que aparecer um status code no código, aponte pra tabela. Em 20 minutos os alunos começam a falar "deu 404" naturalmente.

#### Como ver o status code no Python

```python
import requests

resposta = requests.get("https://viacep.com.br/ws/01001000/json/")

print(resposta.status_code)   # 200 se deu certo
print(resposta.ok)            # True se for 2xx, False caso contrário
```

> *"Todo objeto `resposta` que o `requests.get()` devolve tem um `.status_code`. Antes de fazer `resposta.json()`, sempre dá pra conferir o código."*

---

### 🎯 Exercício Relâmpago 3.5A — Descobrindo Status Codes *(~5 min)*

> No terminal (ou num arquivo `testes_status.py`), execute essas três chamadas e anote o status code de cada uma:
>
> ```python
> import requests
>
> # Teste 1 — URL correta
> r1 = requests.get("https://viacep.com.br/ws/01001000/json/")
> print("Teste 1:", r1.status_code)
>
> # Teste 2 — URL com recurso inexistente
> r2 = requests.get("https://viacep.com.br/ws/99999999/json/")
> print("Teste 2:", r2.status_code)
>
> # Teste 3 — URL errada (endpoint que não existe)
> r3 = requests.get("https://viacep.com.br/ws/endpoint_inventado/")
> print("Teste 3:", r3.status_code)
> ```
>
> ✅ Critério: o aluno consegue explicar em uma frase por que cada código apareceu.

> 💡 **Surpresa pedagógica:** O teste 2 do ViaCEP devolve **200** com `{"erro": true}` no corpo — não 404! Isso é um ótimo gancho pra explicar que nem toda API usa status codes "direito". Algumas APIs mais antigas retornam 200 pra tudo e colocam o erro no JSON. Faz parte da vida.

---

### 3.5.2 Cache no Streamlit — `@st.cache_data` (~10 min)

Antes de começar a trabalhar com APIs autenticadas, um problema chato aparece: o Streamlit reroda o script inteiro a cada interação. Isso significa que **cada clique, cada digitação, cada ajuste no código vai refazer a chamada da API**.

Isso é ruim por três motivos:

1. **Lentidão** — sua interface fica travada esperando a rede toda hora
2. **Limite de uso** — a maioria das APIs limita quantas chamadas você pode fazer por dia
3. **Boas maneiras** — não se deve martelar um servidor alheio à toa

A solução do Streamlit é um decorator chamado `@st.cache_data`. Você coloca ele em cima de uma função, e o Streamlit memoriza o resultado. Se você chamar a função com os mesmos argumentos de novo, ele devolve a resposta guardada — sem refazer a chamada.

#### Exemplo rápido — sem cache vs. com cache

```python
import streamlit as st
import requests
import time

# SEM cache — toda vez que rerodar, chama a API
def buscar_cep_lento(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    return requests.get(url).json()

# COM cache — chama a API uma vez, depois guarda
@st.cache_data
def buscar_cep_rapido(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    return requests.get(url).json()

# Teste: digite qualquer coisa e veja o tempo de resposta
cep = st.text_input("CEP:")

if cep:
    inicio = time.time()
    dados = buscar_cep_rapido(cep)
    fim = time.time()
    st.write(f"Demorou {(fim - inicio)*1000:.0f}ms")
    st.json(dados)
```

Rode e digite um CEP. A primeira vez demora uns 200-500ms (chamada de rede de verdade). A segunda vez com o mesmo CEP demora **menos de 1ms** — veio do cache.

#### Quando usar `@st.cache_data`

- ✅ Funções que fazem chamadas HTTP
- ✅ Funções que leem arquivos grandes
- ✅ Funções que calculam algo pesado
- ❌ Funções que dependem da hora atual ou de aleatoriedade (o cache vai congelar o resultado)
- ❌ Funções que retornam objetos não-serializáveis (conexões de banco, sockets, etc.)

> 💡 **Sacada pro professor:** Mostre ao vivo a diferença. Rode um app sem cache fazendo 3 chamadas — fica travando. Adicione o decorator, rode de novo — instantâneo. O "aha moment" é forte.

> ⚠️ **Aviso:** o cache dura enquanto o app está rodando. Quando reinicia (ou quando o Streamlit Cloud dorme), o cache some. Pra uso em aula, é perfeito. Pra produção existem configurações de TTL (tempo de vida), mas por ora ignora.

---

### 3.5.3 Apresentando a API do TMDB

Até agora todas as APIs que vimos eram abertas: qualquer pessoa, com qualquer URL, podia chamar. Isso funciona pra serviços simples (CEP, país), mas a maioria das APIs comerciais **precisa saber quem está chamando**. Duas razões:

- **Controle de uso** — cada usuário tem um limite mensal
- **Rastreabilidade** — se alguém abusa, dá pra bloquear

A forma mais comum de fazer isso é com uma **API key** — um código único que identifica você. E o jeito profissional de mandar essa chave é no **header da requisição**, não na URL.

#### O que é a TMDB

A **The Movie Database (TMDB)** é uma base de dados colaborativa de filmes e séries, tipo um IMDb aberto. Tem uma API gratuita com cadastro simples que devolve tudo: título, sinopse, pôster, nota, elenco — inclusive **em português**.

> 💡 Essa API é o que muitos apps reais de catálogo de filmes usam por trás. É perfeita pra gente porque: (1) é gratuita, (2) tem tradução pt-BR, (3) devolve URLs de imagens lindas, (4) usa header auth, que é o padrão profissional.

#### Passo a passo do cadastro *(fazer em aula, ao vivo)*

1. Acesse **https://www.themoviedb.org/signup**
2. Preenche nome de usuário, senha, email. Confirma o email.
3. Depois de logado, vai em **Configurações → API** (ou direto em `themoviedb.org/settings/api`)
4. Clica em **Solicitar uma chave de API**
5. Escolhe a opção **"Desenvolvedor"** (gratuita)
6. Preenche o formulário — tipo de aplicação: `Website`, finalidade: `Educational / Student project`, descrição: qualquer coisa honesta
7. Aceita os termos
8. **Pronto.** Aparecem duas chaves: uma `API Key (v3 auth)` e um **`API Read Access Token` (v4 auth)** — vamos usar o segundo, que é o padrão moderno

> 💡 **Sacada pro professor:** Deixe esse passo como lição de casa da aula anterior, ou tenha um plano B: crie uma conta "da turma" com antecedência e deixe a chave no `secrets.toml` da máquina do professor pra quem não conseguir se cadastrar. Também anuncie com antecedência: "aula que vem precisa de email de confirmação pronto".

---

### 3.5.4 Primeira chamada — explorando no terminal

Como sempre: **terminal primeiro, interface depois.** Crie um arquivo `testa_tmdb.py`.

```python
import requests

# Cole seu Read Access Token aqui TEMPORARIAMENTE
# Vamos mover pra secrets.toml mais pra frente
TOKEN = "cole_aqui_seu_token_v4"

url = "https://api.themoviedb.org/3/search/movie"

# PARÂMETROS: viram ?chave=valor na URL final
params = {
    "query": "matrix",       # o que procurar
    "language": "pt-BR",     # idioma da resposta
    "page": 1                # página de resultados
}

# HEADERS: metadados da requisição — autenticação vai aqui
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "accept": "application/json"
}

resposta = requests.get(url, headers=headers, params=params)

print("Status:", resposta.status_code)
print("JSON:", resposta.json())
```

> *"Repare na diferença: antes a gente montava a URL com f-string. Agora passamos `params` como dicionário e o `requests` constrói a URL sozinho. Mais seguro (escapa caracteres especiais) e mais legível."*

Rode. Se der **200**, o JSON vai aparecer. Se der **401**, a chave tá errada — confere o token.

#### Entendendo o que veio

```python
# ... (continua do arquivo)
dados = resposta.json()

print("Chaves do JSON:", dados.keys())
# dict_keys(['page', 'results', 'total_pages', 'total_results'])

print("Total de resultados:", dados["total_results"])
print("Filmes nesta página:", len(dados["results"]))

# Explora o primeiro filme
primeiro = dados["results"][0]
for chave in primeiro.keys():
    print(" ", chave)
```

Rode. Vão aparecer chaves como `title`, `overview`, `release_date`, `vote_average`, `poster_path`, `genre_ids`. Peça aos alunos que descubram o que cada campo significa olhando o próprio JSON.

#### Montando a URL do pôster

O TMDB não te devolve a URL completa da imagem. Ele devolve só um caminho tipo `/9fA2tM2p6P2d5dWQn5bKZP7d5Za.jpg`, e você precisa prefixar com o CDN:

```python
base_imagem = "https://image.tmdb.org/t/p/w500"
poster_path = primeiro["poster_path"]
url_poster = f"{base_imagem}{poster_path}"
print("Pôster:", url_poster)
```

Cole a URL no navegador. O pôster aparece.

> 💡 **O padrão "base + path":** muitas APIs fazem isso pra economizar banda e permitir mudar o CDN sem quebrar respostas antigas. O `w500` é a largura em pixels — existe `w200`, `w780`, `original`, etc.

---

### 3.5.5 Construindo o app Streamlit

Agora que os dados saem certo no terminal, vamos pro Streamlit. Crie `app_tmdb.py`.

#### Passo 1 — Estrutura e sidebar

```python
import streamlit as st
import requests

# Por enquanto deixa a chave aqui — migramos depois
TOKEN = "cole_aqui_seu_token_v4"

st.set_page_config(page_title="Buscador de Filmes", page_icon="🎬", layout="wide")

st.title("🎬 Buscador de Filmes")
st.write("Busque informações sobre qualquer filme usando a API do TMDB.")

# ── SIDEBAR ──────────────────────────────────────────
# Tudo que está em st.sidebar aparece na barra lateral esquerda.
# Ótimo para filtros e configurações que não são a ação principal.
with st.sidebar:
    st.header("⚙️ Filtros")

    idioma = st.selectbox(
        "Idioma da resposta:",
        options=["pt-BR", "en-US", "es-ES"],
        index=0
    )

    max_resultados = st.slider(
        "Quantos resultados mostrar:",
        min_value=1, max_value=10, value=5
    )

    st.markdown("---")
    st.caption("Dados fornecidos por [TMDB](https://themoviedb.org)")
```

Rode. A sidebar aparece do lado esquerdo, a tela principal fica mais ampla por causa do `layout="wide"`.

> 💡 `layout="wide"` muda o conteúdo principal pra usar toda a tela. Por padrão o Streamlit centraliza numa faixa estreita — pra apps com imagens e colunas, wide fica muito melhor.

---

#### Passo 2 — Função de busca com cache

```python
# ... (código anterior)

# Essa função vai ser cacheada — se chamarem com os mesmos argumentos,
# o Streamlit devolve o resultado guardado em vez de chamar a API de novo
@st.cache_data
def buscar_filmes(query, idioma):
    url = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "accept": "application/json"
    }
    params = {
        "query": query,
        "language": idioma,
        "page": 1
    }
    resposta = requests.get(url, headers=headers, params=params)

    # Retornamos uma tupla (dados, erro) — padrão que já vimos no ex_consulta_cnpj
    if resposta.status_code == 401:
        return None, "Chave de API inválida. Confira o token."
    if resposta.status_code == 429:
        return None, "Muitas requisições. Espere um minuto."
    if resposta.status_code != 200:
        return None, f"Erro na API (status {resposta.status_code})."

    return resposta.json(), None
```

> *"Reparem: a mesma função poderia servir qualquer API autenticada por Bearer token. É o mesmo padrão do ex_consulta_cnpj, só muda o endpoint e os parâmetros. Esse esqueleto vai aparecer no trabalho de vocês, no estágio, no projeto pessoal."*

---

#### Passo 3 — Input principal e listagem de resultados

```python
# ... (continua)

# ── ÁREA PRINCIPAL ─────────────────────────────────────
busca = st.text_input(
    "Nome do filme:",
    placeholder="Ex: Matrix, Vingadores, Cidade de Deus..."
)

if st.button("🔎 Buscar") and busca:

    with st.spinner("Buscando na base do TMDB..."):
        dados, erro = buscar_filmes(busca, idioma)

    if erro:
        st.error(f"❌ {erro}")
    elif not dados["results"]:
        st.warning(f"Nenhum filme encontrado para '{busca}'.")
    else:
        total = dados["total_results"]
        st.success(f"✅ {total} filme(s) encontrado(s). Mostrando até {max_resultados}:")

        # Pegamos só até max_resultados filmes
        filmes = dados["results"][:max_resultados]

        # Por enquanto mostra tudo feio pra confirmar que funciona
        for filme in filmes:
            st.write(f"**{filme['title']}** ({filme.get('release_date', '—')[:4]})")
            st.write(filme.get('overview', 'Sem sinopse.'))
            st.divider()
```

Rode, busca "matrix". Vai aparecer feio, mas funcionando. Esse é o momento importante: **confirma que os dados chegam antes de decorar.**

---

#### Passo 4 — Layout bonito em duas colunas

Substitua o loop `for filme in filmes` pelo bloco abaixo:

```python
        BASE_IMG = "https://image.tmdb.org/t/p/w300"

        for filme in filmes:
            with st.container(border=True):
                col1, col2 = st.columns([1, 3])

                with col1:
                    poster = filme.get("poster_path")
                    if poster:
                        st.image(f"{BASE_IMG}{poster}", width=180)
                    else:
                        st.caption("Sem pôster disponível")

                with col2:
                    titulo = filme["title"]
                    original = filme.get("original_title", "")
                    ano = filme.get("release_date", "")[:4] or "—"
                    nota = filme.get("vote_average", 0)
                    votos = filme.get("vote_count", 0)
                    sinopse = filme.get("overview") or "_Sinopse indisponível neste idioma._"

                    st.subheader(f"{titulo} ({ano})")

                    if original and original != titulo:
                        st.caption(f"Título original: *{original}*")

                    # Métricas lado a lado
                    m1, m2 = st.columns(2)
                    m1.metric("⭐ Nota", f"{nota:.1f}/10")
                    m2.metric("🗳️ Votos", f"{votos:,}".replace(",", "."))

                    st.markdown("**Sinopse:**")
                    st.write(sinopse)
```

Rode. Agora sim — os resultados aparecem num card com pôster à esquerda, infos à direita, e um separador visual entre filmes.

> 💡 `st.container(border=True)` desenha a borda do card automaticamente — disponível a partir do Streamlit 1.29. Se estiver numa versão antiga, remove o `border=True`, fica sem borda mas funciona igual.

---

#### Passo 5 — Tratando a falta de resultados elegantemente

Adicione logo no início do bloco de resultados, **antes** do `for`:

```python
        if len(filmes) < max_resultados:
            st.info(
                f"ℹ️ A API retornou apenas {len(filmes)} resultado(s) "
                f"(você pediu até {max_resultados})."
            )
```

Pequeno detalhe que faz muita diferença — o usuário entende por que pediu 10 mas só vieram 3.

---

### 🎯 Mini-Desafio 3.5B — Filtro por nota mínima *(~15 min)*

> Adicione na sidebar do app TMDB um `st.slider` chamado "Nota mínima" (0.0 a 10.0, passo 0.5, valor inicial 0.0).
>
> No código que exibe os filmes, filtre para mostrar **apenas os filmes com nota maior ou igual** ao valor escolhido.
>
> Se nenhum filme da busca passar no filtro, mostre um `st.warning` dizendo isso.
>
> ✅ Critério: ao subir o slider pra 8.0, só aparecem filmes com nota ≥ 8. Buscas populares como "matrix" devem deixar de mostrar resultados obscuros.

---

### 3.5.6 Último passo — Movendo a chave pro `secrets.toml`

Agora que o app funciona 100%, vamos resolver o problema da chave estar solta no código.

> *"Por que isso é importante? Porque no próximo bloco vocês vão publicar o app no GitHub. Se o token estiver no código, qualquer pessoa que encontrar o repositório vai poder usar a conta de vocês — e em APIs pagas, isso vira prejuízo real. É prática profissional básica: **credenciais nunca vão pro código-fonte**."*

#### A mudança ao vivo

**Passo 1** — Na pasta do projeto, crie a estrutura:

```
app_tmdb.py
.streamlit/
    └── secrets.toml
```

> ⚠️ O `.streamlit` começa com ponto — em alguns sistemas é considerado pasta oculta. Normal.

**Passo 2** — Dentro de `secrets.toml`:

```toml
# .streamlit/secrets.toml
TMDB_TOKEN = "cole_aqui_seu_token_v4_completo"
```

**Passo 3** — No `app_tmdb.py`, **apague** a linha `TOKEN = "cole_aqui..."` e substitua no header da função por:

```python
headers = {
    "Authorization": f"Bearer {st.secrets['TMDB_TOKEN']}",
    "accept": "application/json"
}
```

**Passo 4** — Rode de novo. Continua funcionando **exatamente igual**. A chave saiu do código sem quebrar nada.

**Passo 5** — Se você vai subir pro GitHub, crie um `.gitignore` na raiz com:

```
.streamlit/secrets.toml
```

Isso evita que o arquivo com o token seja enviado junto quando der `git push`.

> 💡 **Sacada pedagógica:** Faça essa migração **depois** do app funcionar, não antes. Deixar a chave no código 40 minutos e depois "esconder" gera um aha moment que explicar em teoria não produz. Os alunos entendem o **propósito** do `secrets.toml`, não só o ritual.

---

### 3.5.7 Recapitulando o bloco

Nesse bloco a gente:

- Entendeu **status codes HTTP** — 200, 401, 404, 500 e companhia
- Aprendeu a usar **`@st.cache_data`** pra não martelar a API a cada rerun
- Fez a primeira chamada com **autenticação por header** (Bearer token)
- Passou **parâmetros** via dicionário em vez de f-string na URL
- Construiu um app com **sidebar** (`st.sidebar`) e **layout wide** (`st.set_page_config`)
- Organizou resultados em **cards com colunas de proporção diferente** (`st.columns([1, 3])`)
- Moveu credenciais do código pro **`secrets.toml`** — prática profissional

Esse esqueleto — chave no secrets + função cacheada + padrão `(dados, erro)` + layout com sidebar — serve pra qualquer API autenticada que vocês encontrarem. TMDB hoje, Spotify amanhã, IA depois. O padrão não muda.

---

### 🎯 Mini-Desafio 3.5C — Mudando de API com o mesmo esqueleto *(opcional, ~15 min)*

> O TMDB tem um endpoint separado pra séries de TV, quase idêntico ao de filmes:
>
> `https://api.themoviedb.org/3/search/tv` — usa o mesmo token, os mesmos params, e devolve JSON parecido (a diferença é que o campo `title` vira `name` e `release_date` vira `first_air_date`).
>
> **Desafio:** adicione na sidebar um `st.radio` com opções "Filmes" e "Séries". Faça a função `buscar_filmes` virar `buscar` e receber o tipo, mudando o endpoint e os campos conforme a escolha.
>
> ✅ Critério: ao alternar entre Filmes e Séries com a mesma busca, os resultados mudam corretamente — e o cache funciona pra cada combinação.
