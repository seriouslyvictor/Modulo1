import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x200")

def saudar():
    label_resultado.configure(text="Olá! Botão funcionou!")

botao = ctk.CTkButton(app, text="Clique", command=saudar)
botao.pack(pady=10)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack(pady=10)

app.mainloop()
