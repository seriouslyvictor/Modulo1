import streamlit as st
import requests

# ─────────────────────────────────────────────
# EXERCÍCIO — Consulta de CNPJ
# API: https://brasilapi.com.br/api/cnpj/v1/{cnpj}
# Sem autenticação. Método: GET
#
# A API aceita os formatos:
#   Só números:               00000000000000
#   Pontuação completa:       00.000.000/0000-00
#   Pontos e barra sem hífen: 00.000.000/000000
#
# Por boa prática, a gente limpa e valida no cliente
# antes de qualquer chamada à rede.
# ─────────────────────────────────────────────


# ── FUNÇÕES ──────────────────────────────────

def limpar_cnpj(cnpj):
    """Remove pontuação do CNPJ e devolve só os dígitos."""
    return cnpj.replace(".", "").replace("/", "").replace("-", "").strip()


def cnpj_valido(cnpj_limpo):
    """
    Retorna True se o CNPJ tem 14 dígitos numéricos.
    Não faz validação matemática — só checa o formato.
    """
    return len(cnpj_limpo) == 14 and cnpj_limpo.isdigit()


def buscar_cnpj(cnpj_limpo):
    """
    Chama a BrasilAPI com o CNPJ limpo.
    Retorna (dados, erro):
      - dados: dicionário com os dados da empresa, ou None
      - erro:  string com a mensagem de erro, ou None
    """
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"

    try:
        resposta = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
        return None, "Sem conexão com a internet."

    if resposta.status_code == 404:
        return None, "CNPJ não encontrado na Receita Federal."

    if resposta.status_code != 200:
        return None, f"Erro na API: status {resposta.status_code}"

    return resposta.json(), None


def formatar_telefone(tel):
    """Recebe um dict de telefone e devolve uma string formatada."""
    tipo = "Fax" if tel.get("is_fax") else "Telefone"
    return f"**{tipo}:** ({tel['ddd']}) {tel['numero']}"


def formatar_cep(cep):
    """Recebe um CEP como string de 8 dígitos e devolve 00000-000."""
    if len(cep) == 8:
        return f"{cep[:5]}-{cep[5:]}"
    return cep  # devolve como veio se não tiver 8 dígitos


def montar_endereco(dados):
    """Monta a linha de logradouro a partir das chaves do dict da API."""
    tipo = dados.get("tipo_logradouro", "")
    logradouro = dados.get("logradouro", "")
    numero = dados.get("numero", "")
    complemento = dados.get("complemento", "").strip()

    linha = f"{tipo} {logradouro}, {numero}"
    if complemento:
        linha += f" — {complemento}"
    return linha


# ── INTERFACE ─────────────────────────────────

st.title("🏢 Consulta de CNPJ")
st.write("Digite um CNPJ para verificar se ele é válido e ver as informações da empresa.")

cnpj_digitado = st.text_input("CNPJ:", placeholder="Ex: 07.329.573/0003-74")

if st.button("Consultar"):

    cnpj_limpo = limpar_cnpj(cnpj_digitado)

    if not cnpj_valido(cnpj_limpo):
        st.error("❌ CNPJ inválido — deve ter 14 dígitos numéricos.")

    else:
        with st.spinner("Consultando Receita Federal..."):
            dados, erro = buscar_cnpj(cnpj_limpo)

        if erro:
            st.error(f"❌ {erro}")

        else:
            # ── SITUAÇÃO ─────────────────────────────
            situacao = dados.get("situacao_cadastral", "Desconhecida")
            if situacao == "Ativa":
                st.success(f"✅ CNPJ válido — Situação: {situacao}")
            else:
                st.warning(f"⚠️ CNPJ encontrado, mas situação: {situacao}")

            st.divider()

            # ── IDENTIFICAÇÃO ────────────────────────
            st.subheader("Identificação")
            col1, col2 = st.columns(2)
            col1.metric("CNPJ", dados["cnpj"])
            col2.metric("Tipo", dados.get("matriz_filial", "—"))

            razao = dados.get("razao_social", "—")
            fantasia = dados.get("nome_fantasia", "")
            st.write(f"**Razão Social:** {razao}")
            if fantasia:
                st.write(f"**Nome Fantasia:** {fantasia}")

            st.write(f"**Natureza Jurídica:** {dados.get('natureza_juridica', '—')}")
            st.write(f"**Porte:** {dados.get('porte_empresa', '—')}")
            st.write(f"**Início das Atividades:** {dados.get('data_inicio_atividade', '—')}")

            st.divider()

            # ── ENDEREÇO ─────────────────────────────
            st.subheader("Endereço")
            st.write(f"**Logradouro:** {montar_endereco(dados)}")
            st.write(f"**Bairro:** {dados.get('bairro', '—')}")

            col3, col4 = st.columns(2)
            col3.metric("Município", dados.get("municipio", "—"))
            col4.metric("UF", dados.get("uf", "—"))

            st.write(f"**CEP:** {formatar_cep(dados.get('cep', ''))}")

            st.divider()

            # ── CONTATO ──────────────────────────────
            st.subheader("Contato")
            email = dados.get("email", "")
            if email:
                st.write(f"**E-mail:** {email.lower()}")

            telefones = dados.get("telefones", [])
            for tel in telefones:
                st.write(formatar_telefone(tel))

            st.divider()

            # ── QUADRO SOCIETÁRIO (QSA) ───────────────
            socios = dados.get("QSA", [])
            if socios:
                st.subheader(f"Quadro Societário ({len(socios)} pessoa(s))")
                for socio in socios:
                    with st.expander(socio.get("nome_socio", "Sócio")):
                        st.write(f"**Qualificação:** {socio.get('qualificacao_socio', '—')}")
                        st.write(f"**Tipo:** {socio.get('identificador_socio', '—')}")
                        st.write(f"**Faixa Etária:** {socio.get('faixa_etaria', '—')}")
                        st.write(f"**Entrada na Sociedade:** {socio.get('data_entrada_sociedade', '—')}")
