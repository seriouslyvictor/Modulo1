import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x250")

def mostrar_nome():
    nome = entrada_nome.get()
    label_resultado.configure(text=f"Seu nome é: {nome}")

label = ctk.CTkLabel(app, text="Digite seu nome:")
label.pack(pady=5)

entrada_nome = ctk.CTkEntry(app, width=200)
entrada_nome.pack(pady=5)

botao = ctk.CTkButton(app, text="Confirmar", command=mostrar_nome)
botao.pack(pady=10)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack(pady=5)

app.mainloop()
