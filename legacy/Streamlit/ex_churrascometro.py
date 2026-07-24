import streamlit as st

st.title("Churrascômetro 2.0")
st.write("Descubra quanto comprar para o seu churrasco!")

# -------------------------------------------------------------------
# INPUTS
# st.number_input cria um campo numérico com valor mínimo e padrão.
# O valor digitado pelo usuário fica salvo na variável automaticamente.
# -------------------------------------------------------------------
adultos = st.number_input("Número de adultos", min_value=0, value=0, step=1)
criancas = st.number_input("Número de crianças", min_value=0, value=0, step=1)

# -------------------------------------------------------------------
# FÓRMULAS VISÍVEIS
# st.info() exibe um bloco azul informativo — ótimo para mostrar regras.
# -------------------------------------------------------------------
st.info("""
**Fórmulas usadas no cálculo:**
- 🥩 Carne: 300g por adulto / 150g por criança
- 🥤 Bebidas: 1,5L por adulto / 0,75L por criança
- 🥗 Acompanhamentos: 200g por pessoa (adultos e crianças)
""")

# -------------------------------------------------------------------
# BOTÃO
# st.button() retorna True apenas no momento em que for clicado.
# Todo o código dentro do "if" só executa quando o usuário clicar.
# -------------------------------------------------------------------
if st.button("Calcular Churrasco"):

    # --- Cálculos ---
    # Convertemos gramas para kg dividindo por 1000,
    # assim o resultado fica mais legível para o usuário.
    carne_kg = (adultos * 300 + criancas * 150) / 1000
    bebidas_l = adultos * 1.5 + criancas * 0.75
    acomp_kg = (adultos + criancas) * 200 / 1000

    # --- Resultados ---
    # st.metric() exibe um valor grande e destacado — perfeito para resultados.
    # Parâmetros: label (título), value (valor exibido).
    # Usamos colunas (st.columns) para mostrar as três métricas lado a lado.
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🥩 Carne", f"{carne_kg:.2f} kg")

    with col2:
        st.metric("🥤 Bebidas", f"{bebidas_l:.1f} L")

    with col3:
        st.metric("🥗 Acompanhamentos", f"{acomp_kg:.2f} kg")
