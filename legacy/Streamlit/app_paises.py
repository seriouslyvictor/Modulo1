import streamlit as st
import requests, locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# ─────────────────────────────────────────────
# ETAPA 2 — Buscador de Países (com Streamlit)
# API: https://restcountries.com/v3.1/name/{pais}
# Sem autenticação. Método: GET
#
# Construído em 3 passos — veja os comentários
# marcados com PASSO 1, PASSO 2, PASSO 3.
# ─────────────────────────────────────────────

st.title("🌍 Buscador de Países")
st.write("Digite o nome de um país em inglês para ver suas informações.")

# ── PASSO 1 — Estrutura básica com input e botão ─────────────

nome = st.text_input("Nome do país:", placeholder="Ex: brazil, france, japan")

if st.button("Buscar"):
    if not nome:
        st.error("Digite o nome de um país primeiro!")

    # ── PASSO 2 — Chamar a API e tratar país não encontrado ──

    else:
        url = f"https://restcountries.com/v3.1/translation/{nome}"

        with st.spinner("Buscando informações..."):
            resposta = requests.get(url)

        if resposta.status_code == 404:
            st.error(f"País '{nome}' não encontrado. Verifique o nome em inglês.")

        # ── PASSO 3 — Extrair os dados e exibir com widgets ──

        else:
            dados = resposta.json()
            pais_info = dados[0]

            # Extração — igual ao que fizemos no terminal (busca_pais.py)
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

            # st.columns([1, 2]) cria duas colunas com proporções diferentes
            # a segunda é o dobro da primeira — ótimo para imagem ao lado de texto
            col1, col2 = st.columns([1, 2])

            
            col1.image(bandeira, width=180)

            col2.subheader(nome_pt)
            col2.metric("Capital", capital)
            col2.metric("População", f"{populacao:n}")

            st.divider()

            st.write(f"**Idiomas:** {idiomas_str}")
            st.write(f"**Moeda:** {moedas_str}")
