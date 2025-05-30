from flask import Flask, render_template, request, abort
import json, os
app = Flask(__name__)

users =[{"perfil": "Thea", "seguidores": 50, "seguindo": 250, "publicações": 38}, {"perfil": "Theo", "seguidores": 150, "seguindo": 5, "publicações": 50}]
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/users')
def display_users(profiles=None):
    return render_template("users.html", profiles=users)

@app.route("/users/<username>")
def display_user(username):
    user = None
    for item in users:
        if item["perfil"].lower() == username.lower():
            user = item
            break
    if user:
        return render_template("single.html", user=user)
    else:
        return render_template("index.html")

@app.route("/submit", methods=["POST", "GET"])
def receber_dados():
    if request.method == "GET":
        return render_template("index.html")
    try:
        with open(file="Webserver/leads.json", mode="r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    
    form_data = {request.form["nome"]: {"email": request.form["email"], "zaperson": request.form["senha"]}}
    existing_data.update(form_data)
    
    with open(file="Webserver/leads.json", mode="w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)