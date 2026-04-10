import requests
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
# ─────────────────────────────────────────────
# ETAPA 1 — Buscador de Países (só terminal)
# API: https://restcountries.com/v3.1/name/{pais}
# Sem autenticação. Método: GET
#
# Objetivo: extrair os dados corretamente antes
# de pensar em qualquer interface visual.
# ─────────────────────────────────────────────


# ── BLOCO 1 — Fazer a chamada e ver o que chega ──────────────

pais = "brazil"
url = f"https://restcountries.com/v3.1/name/{pais}"

resposta = requests.get(url)
dados = resposta.json()

print(type(dados))   # <class 'list'>  — a resposta é uma LISTA
print(len(dados))    # quantos países vieram?

# ── BLOCO 2 — Entrar no primeiro item da lista ───────────────

# dados é uma lista — pegamos o primeiro item com [0]
pais_info = dados[0]

# Imprime todas as chaves disponíveis nesse dicionário
print("\nChaves disponíveis:")
for chave in pais_info.keys():
    print(" ", chave)

# ── BLOCO 3 — Extrair os campos simples ──────────────────────

# Nome oficial em português — está dentro de translations > por > official
nome_pt = pais_info["translations"]["por"]["official"]

# População — número direto
populacao = pais_info["population"]

# Capital — é uma lista, pegamos a primeira posição
capital = pais_info["capital"][0]

print(f"\nNome oficial (PT): {nome_pt}")
print(f"População:         {populacao:n}")
print(f"Capital:           {capital}")

# ── BLOCO 4 — Extrair idiomas (dicionário → loop) ────────────

# languages é um dicionário: {"por": "Portuguese", "eng": "English", ...}
# Queremos só os nomes, não os códigos
idiomas = pais_info["languages"]

print("\nIdiomas:")
for codigo, nome in idiomas.items():
    print(f"  - {nome}")

# ── BLOCO 5 — Extrair moeda (dicionário de dicionários) ──────

# currencies é um dicionário de dicionários:
# {"BRL": {"name": "Brazilian real", "symbol": "R$"}}
moedas = pais_info["currencies"]

print("\nMoedas:")
for codigo, info in moedas.items():
    print(f"  - {info['name']} ({info['symbol']})")

# ── BLOCO 6 — Pegar a URL da bandeira ────────────────────────

# flags tem as URLs das imagens da bandeira
bandeira_url = pais_info["flags"]["png"]

print(f"\nBandeira: {bandeira_url}")
# Cole essa URL no navegador — a bandeira vai aparecer!

# ── RESULTADO FINAL — Tudo junto e organizado ────────────────

print("\n" + "=" * 45)
print("RESULTADO FINAL")
print("=" * 45)

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

print(f"Nome oficial: {nome_pt}")
print(f"Capital:      {capital}")
print(f"População:    {populacao:n}")
print(f"Idiomas:      {idiomas_str}")
print(f"Moeda:        {moedas_str}")
print(f"Bandeira:     {bandeira}")
