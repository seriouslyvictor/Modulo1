import streamlit as st
import requests

# Por enquanto deixa a chave aqui — migramos depois
TOKEN = st.secrets["TMDB"]

st.set_page_config(page_title="Buscador de Filmes", page_icon="🎬", layout="wide")

st.title("Buscador de Filmes")
st.write("Busque informações sobre qualquer filme usando a API do TMDB.")



## Barra lateral com as opções de pesquisa
with st.sidebar:
    st.header("Filtros")
    idioma = st.selectbox("Idioma da pesquisa", options=["pt-BR", "en-US"])
    max_resultados = st.slider("Resultados por pesquisa", min_value=1, max_value=10, value=3)
    
    st.info("""Dados fornecidos pelo TMDB 
            Projeto de uso EDUCACIONAL
            https://themoviedb.org
            """)
    
@st.cache_data
def buscar_filmes(filme, idioma):
    url = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "accept": "application/json"
    }

    params = {
        "query": filme,
        "language": idioma,
    }

    resposta = requests.get(url, headers=headers, params=params)
    if resposta.status_code != 200:
        return "Erro na API!"
    
    return resposta.json()

busca = st.text_input("Nome do filme:", placeholder="NARUTO")

if st.button( "Buscar!", icon=":material/search:", type="primary"):
    with st.spinner("Buscando o filme..."):
        dados = buscar_filmes(busca, idioma)
        filmes = dados["total_results"]

    if dados == "Erro na API!":
        st.error("Erro na busca, por favor tente novamente")
    elif not dados:
        st.warning(f"Nenhum filme encontrado com esse nome: {busca}")
    else:
        st.metric(value=f"{max_resultados}/{filmes}", label="Exibindo")
        filmes = dados["results"][:max_resultados]
        for filme in filmes:
            
            titulo = filme.get("title", "Desconhecido")
            data = filme.get("release_date", "Sem data")
            votos = filme.get("vote_count", "?")
            rating = round(filme.get("vote_average", "?"),2)
            st.subheader(f"Nome: {titulo} - {data}")
            col1, col2 = st.columns(2, width=400, )
            col1.metric(value=f"{rating}/10", label="Avaliação", border=True)
            col2.metric(value=votos, label="Votos", border=True)
            st.write(filme.get('overview', "Sem sínopse"))
            st.divider()
    