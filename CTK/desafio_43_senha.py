import customtkinter as ctk

app = ctk.CTk()
app.title("Desafio 4.3 — Verificador de Senha")
app.geometry("400x280")

ctk.CTkLabel(app, text="Digite a senha:").pack(pady=(20, 5))
entrada_senha1 = ctk.CTkEntry(app, width=250, show="*")
entrada_senha1.pack()

ctk.CTkLabel(app, text="Confirme a senha:").pack(pady=(10, 5))
entrada_senha2 = ctk.CTkEntry(app, width=250, show="*")
entrada_senha2.pack()

def verificar():
    if entrada_senha1.get() == entrada_senha2.get():
        label_resultado.configure(text="✅ Senhas iguais!", text_color="lightgreen")
    else:
        label_resultado.configure(text="❌ Senhas diferentes!", text_color="orange")

ctk.CTkButton(app, text="Verificar", command=verificar).pack(pady=15)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack()

app.mainloop()
