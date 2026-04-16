from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    exercicios = [
        {"titulo": "1a - Cartao de Perfil estilo Instagram", "endpoint": "perfil"},
        {"titulo": "1b - Cartao de Produto (iPhone)", "endpoint": "produto"},
        {"titulo": "1c - Recibo de Pedido", "endpoint": "pedido"},
        {"titulo": "2a - Candidatos Aprovados", "endpoint": "aprovados"},
        {"titulo": "2b - Playlist", "endpoint": "playlist"},
        {"titulo": "2c - Nota de Serie da Netflix", "endpoint": "serie"},
        {"titulo": "3a - Perfil com Idade", "endpoint": "perfil_idade"},
        {"titulo": "3b - Pagina de Clima", "endpoint": "clima"},
        {"titulo": "3c - Extrato Pix", "endpoint": "pix"},
        {"titulo": "4a - Cartao de Pet", "endpoint": "pet"},
        {"titulo": "4b - Sala de Aula", "endpoint": "turma"},
        {"titulo": "4c - Loja", "endpoint": "loja"},
        {"titulo": "4d - Dados Aninhados", "endpoint": "times"},
    ]
    return render_template("index.html", exercicios=exercicios)


@app.route("/perfil")
def perfil():
    nome = "Yukimura Sanada"
    bio = "Aprendendo Flask, HTML e Jinja um passo de cada vez."
    seguidores = 1280
    seguindo = 315
    publicacoes = 42
    return render_template(
        "perfil.html",
        nome=nome,
        bio=bio,
        seguidores=seguidores,
        seguindo=seguindo,
        publicacoes=publicacoes,
    )


@app.route("/produto")
def produto():
    nome_produto = "iPhone 15"
    preco = 5999
    valor_parcela = round(preco / 12, 2)
    descricao = "Tela brilhante, cameras fortes e bateria para o dia inteiro."
    imagem = "/static/images/iphone.avif"
    armazenamento = "256 GB"
    return render_template(
        "produto.html",
        nome_produto=nome_produto,
        preco=preco,
        valor_parcela = valor_parcela,
        descricao=descricao,
        imagem=imagem,
        armazenamento=armazenamento,

    )


@app.route("/pedido")
def pedido():
    nome_item = "Coxinha"
    quantidade = 3
    preco_unitario = 8
    total = quantidade * preco_unitario
    return render_template(
        "pedido.html",
        nome_item=nome_item,
        quantidade=quantidade,
        preco_unitario=preco_unitario,
        total=total,
    )


@app.route("/aprovados")
def aprovados():
    candidatos = [
        "Ana Souza",
        "Bruno Lima",
        "Carlos Melo",
        "Daniela Rocha",
        "Eduarda Alves",
        "Felipe Santos",
        "Giovana Costa",
    ]
    return render_template("aprovados.html", candidatos=candidatos)


@app.route("/playlist")
def playlist():
    musicas = [
        "Tempo Perdido",
        "Ela Partiu",
        "Do I Wanna Know?",
        "As It Was",
        "Trevo",
    ]
    return render_template("playlist.html", musicas=musicas)


@app.route("/serie")
def serie():
    nome_serie = "Stranger Things"
    estrelas = 4
    return render_template("serie.html", nome_serie=nome_serie, estrelas=estrelas)


@app.route("/perfil-idade")
def perfil_idade():
    nome = "Maya"
    idade = 16
    return render_template("perfil_idade.html", nome=nome, idade=idade)


@app.route("/clima")
def clima():
    cidade = "Sao Paulo"
    temperatura = 29
    return render_template("clima.html", cidade=cidade, temperatura=temperatura)


@app.route("/pix")
def pix():
    transacoes = [250, -39, -18, 1200, -250, 90, -10]
    return render_template("pix.html", transacoes=transacoes)


@app.route("/pet")
def pet():
    pet = {"nome": "Rex", "especie": "Cachorro", "idade": 5, "vacinado": True}
    return render_template("pet.html", pet=pet)


@app.route("/turma")
def turma():
    alunos = [
        {"nome": "Alice", "idade": 15, "nota": 9.2},
        {"nome": "Breno", "idade": 16, "nota": 7.5},
        {"nome": "Camila", "idade": 15, "nota": 8.8},
        {"nome": "Diego", "idade": 17, "nota": 6.9},
    ]
    return render_template("turma.html", alunos=alunos)


@app.route("/loja")
def loja():
    produtos = [
        {"nome": "Mouse Gamer", "preco": "R$ 149,90", "em_estoque": True},
        {"nome": "Teclado Mecanico", "preco": "R$ 289,90", "em_estoque": False},
        {"nome": "Headset RGB", "preco": "R$ 219,90", "em_estoque": True},
        {"nome": "Webcam HD", "preco": "R$ 199,90", "em_estoque": False},
    ]
    return render_template("loja.html", produtos=produtos)


@app.route("/times")
def times():
    times = [
        {"nome": "Time Pixel", "membros": ["Lia", "Rafa", "Bianca"]},
        {"nome": "Time Debug", "membros": ["Joao", "Marta"]},
        {"nome": "Time Deploy", "membros": ["Nina", "Caio", "Iris", "Theo"]},
    ]
    return render_template("times.html", times=times)


if __name__ == "__main__":
    app.run(debug=True)
