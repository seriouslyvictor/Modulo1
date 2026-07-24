import streamlit as st
import requests
import json


# Demonstrando diferença de cache
def buscar_cep_lento(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    dados = requests.get(url).json()
    return dados

@st.cache_data
def buscar_cep_rapido(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    dados = requests.get(url).json()
    return dados

cep = st.text_input("CEP:")

if cep:    
    with st.spinner("Rodando....", show_time=True):
        dados = buscar_cep_rapido(cep)
    st.json(dados)

TOKEN = ""

url = "https://api.themoviedb.org/3/search/movie"

params = {     # o que procurar
    "query": "Matrix",
    "language": "pt-BR",     # idioma da resposta
    "sort_by": "vote_average.desc",
    "page": 1                # página de resultados
}

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "accept": "application/json"
}



resposta = requests.get(url, headers=headers, params=params)
dados = resposta.json()
with open(file="dump.json", mode="w", encoding="UTF-8") as file:
    json.dump(fp=file, obj=dados, ensure_ascii=False, indent=4)

print("Chaves do json:", dados.keys())

print("total de resultados:", dados["total_results"])
print("Filmes nessa página:", len(dados["results"]))

primeiro_filme = dados["results"][0]
print(primeiro_filme)

# Montando url do poster para exibir no streamlit:
url_base = "https://image.tmdb.org/t/p/w500"
caminho_poster = primeiro_filme["poster_path"]
url_completa_imagem = f"{url_base}{caminho_poster}"