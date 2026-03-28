import customtkinter as ctk

app = ctk.CTk()
app.title("Desafio 4.5 — Gerador de Apelido")
app.geometry("400x280")

ctk.CTkLabel(app, text="Seu primeiro nome:").pack(pady=(20, 5))
entrada_nome = ctk.CTkEntry(app, width=250, placeholder_text="Ex: Lucas")
entrada_nome.pack()

ctk.CTkLabel(app, text="Categoria:").pack(pady=(10, 5))
opcoes = ctk.CTkOptionMenu(app, values=["Esporte", "Tecnologia", "Anime"])
opcoes.pack()

def gerar_apelido():
    nome = entrada_nome.get().strip()
    categoria = opcoes.get()

    if categoria == "Esporte":
        apelido = f"{nome} Gol de Placa"
    elif categoria == "Tecnologia":
        apelido = f"{nome}.exe"
    else:
        apelido = f"{nome}-kun"

    label_resultado.configure(text=f"Apelido: {apelido}")

ctk.CTkButton(app, text="Gerar Apelido", command=gerar_apelido).pack(pady=15)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack()

app.mainloop()
