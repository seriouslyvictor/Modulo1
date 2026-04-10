import streamlit as st


st.markdown("# Básico/Essenciais")

st.title('Primeiro APP')
st.write("VAAAAI CURINTHIAAA")

st.markdown("**negrito**, *itálico* e até listas!")
st.markdown("""
            - item 1
            - item 2
            - item 3""")

st.image(image="Space Marine.jpg", width=300,)

# Mensagens de status

st.success("Deu bom!")
st.error("Deu ruim!")
st.warning("Presta atenção!")
st.info("Você sabia? as pessoas morrem quando são assassinadas!!")

#Streamlit, sendo voltado para dados, possue visualização rica de números:
st.metric(label="Temperatura", value="28ºC", delta="+3ºC")
st.metric(label="Calorias", value="256kcal")

#Streamlit, rodando na web, faz uso de flex e grids para layouts mais interessantes:
col1, col2, col3 = st.columns(3)

col1.metric(label="Temperatura", value="28ºC", delta="+3ºC")
col2.metric(label="Calorias", value="256kcal")

st.markdown("# Interatividade")
#Interatividade, widgets para pegar dados
nome =  st.text_input("Qual é o seu nome?", placeholder="Braia, atacante do Vasco")
st.write(nome)
tweet = st.text_area("Faça seu tweet!")
st.write(f"Seu tweet tem {len(tweet)}/150 caracteres")
nivel = st.slider("Quantos lanches você vai comer hoje?", min_value=1, max_value=10, value=1)

arquivo = st.file_uploader("Faça upload de uma imagem", type=["png", "jpg", "jpeg"])
if arquivo:
    st.image(arquivo, caption="Sua imagem carregada", width=200)


if st.button("📸 Ligar camera"):
    picture = st.camera_input("Tire uma foto da sua comida")
    if picture:
        st.image(picture, caption="Quem é esse pokemon?", width=200)
        st.success("Pokemon Capturado!")
else:
    st.info("Aperte no botão para ligar sua câmmera")

import time
if st.button("Processar solicitação(2 segundos)"):
    with st.spinner("processando... aguarde", show_time=True, width="stretch"):
        time.sleep(2)
    st.success("Concluído!")

# Mini Desafio
#Churrascometro com metric