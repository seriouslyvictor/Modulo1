import streamlit as st
import requests

st.title("Buscador de CEP")
st.write("Digite um CEP e descubra o endereço completo.")

# -------------------------------------------------------------------
# INPUT
# st.text_input retorna uma string com o que o usuário digitou.
# O placeholder aparece em cinza como dica dentro do campo.
# -------------------------------------------------------------------
cep = st.text_input("Digite o CEP:", placeholder="Ex: 01001-000")

# -------------------------------------------------------------------
# BOTÃO
# Tudo dentro deste "if" só executa quando o usuário clicar no botão.
# -------------------------------------------------------------------
if st.button("Buscar Endereço"):

    if not cep:
        # st.error() exibe uma mensagem vermelha de erro
        st.error("Digite um CEP primeiro!")
    else:
        # -----------------------------------------------------------
        # VALIDAÇÃO DE INPUT
        # st.text_input não tem modo "só números" nativo — o parâmetro
        # type só aceita "default" ou "password". Por isso validamos
        # manualmente com Python puro.
        #
        # .replace() tira traços e espaços que o usuário pode digitar.
        # .isdigit() retorna True se a string contiver apenas números.
        # .len() garante que são exatamente 8 dígitos (tamanho do CEP).
        # -----------------------------------------------------------
        cep_limpo = cep.replace("-", "").replace(" ", "")

        if not cep_limpo.isdigit() or len(cep_limpo) != 8:
            st.error("CEP inválido. Digite apenas os 8 números do CEP.")
            st.stop()  # interrompe a execução sem mostrar mais nada

        # -----------------------------------------------------------
        # CHAMADA À API
        # st.spinner() exibe uma animação de carregamento enquanto
        # o código dentro do "with" está sendo executado.
        # -----------------------------------------------------------
        with st.spinner("Buscando endereço..."):
            url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

            # requests.get() faz uma requisição HTTP GET para a URL.
            # Não precisamos de chave nem de cadastro — é aberta!
            resposta = requests.get(url)

            # .json() converte a resposta em um dicionário Python
            # — exatamente igual a qualquer dict que já usamos antes.
            dados = resposta.json()

        # -----------------------------------------------------------
        # TRATAMENTO DA RESPOSTA
        # Se o CEP não existir, a API retorna {"erro": true}.
        # Precisamos verificar isso antes de tentar ler os outros campos.
        # -----------------------------------------------------------
        if "erro" in dados:
            st.error("CEP não encontrado. Verifique os números.")
        else:
            # st.success() exibe uma mensagem verde de sucesso
            st.success("Endereço encontrado!")

            # st.columns() divide a tela em colunas lado a lado.
            # Aqui criamos 2 colunas para cidade e estado.
            col1, col2 = st.columns(2)
            col1.metric("Cidade", dados["localidade"])
            col2.metric("Estado", dados["uf"])

            # Lemos as outras chaves do dicionário normalmente
            st.write(f"**Logradouro:** {dados['logradouro']}")
            st.write(f"**Bairro:** {dados['bairro']}")
            st.write(f"**CEP formatado:** {dados['cep']}")
