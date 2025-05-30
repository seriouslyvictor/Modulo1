from flask import Flask, render_template, request
import json, os
app = Flask(__name__)

@app.route("/")
def home():
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