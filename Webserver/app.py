from flask import Flask, render_template, request

app = Flask(__name__)

frutas = ["Ovo", "Maçã", "Batata", "Apargos"]

#Rota principal, raiz do site
@app.route("/")
def principal():
    return render_template("index.html")

#Outra rota
@app.route("/sobre")
def sobre():
    return "essa página ainda não existe"

#Rota dinâmica
@app.route("/sobre/<string:pessoa>")
def sobre_pessoa(pessoa):
    return f"Essa é uma página sobre {pessoa}"


@app.route("/surpresa")
def assunto_aleatorio():
    import random
    escolhas = random.choice(["Futebol", "Rugby", "Basquete", "Voleiballz"])
    return f"<h1>Essa é uma página sobre {escolhas}</h1>"

#rotas com frutas
@app.route("/feira", methods=["GET", "POST"])
def carregar_feira():
    if request.method =="POST":
        frutas.append(request.form.get("fruta"))
    return render_template("feira.html", todas_frutas=frutas)

@app.route("/deus")
def carregar_deus():
    deus = {'nome': 'zeus', 'poder': 'raio', 'rank': 1 }
    return render_template('deuses.html', deus=deus)