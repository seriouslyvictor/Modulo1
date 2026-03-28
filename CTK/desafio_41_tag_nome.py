import customtkinter as ctk

app = ctk.CTk()
app.title("Desafio 4.1 — Tag de Nome")
app.geometry("400x250")

ctk.CTkLabel(app, text="Digite seu nome:").pack(pady=10)

entrada_nome = ctk.CTkEntry(app, width=250, placeholder_text="Ex: Carlos")
entrada_nome.pack(pady=5)

def criar_tag():
    nome = entrada_nome.get().strip()
    label_resultado.configure(text=f"Olá! Meu nome é {nome} 👋")

ctk.CTkButton(app, text="Criar Tag", command=criar_tag).pack(pady=10)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack(pady=5)

app.mainloop()
