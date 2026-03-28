import customtkinter as ctk

app = ctk.CTk()
app.title("Desafio 4.7 — App de Recados")
app.geometry("450x400")

ctk.CTkLabel(app, text="Escreva um recado:").pack(pady=(15, 5))

entrada_recado = ctk.CTkEntry(app, width=350, placeholder_text="Digite aqui...")
entrada_recado.pack()

def adicionar():
    recado = entrada_recado.get().strip()
    if recado:
        caixa.insert("end", recado + "\n")
        entrada_recado.delete(0, "end")

def limpar_tudo():
    caixa.delete("0.0", "end")

frame_botoes = ctk.CTkFrame(app, fg_color="transparent")
frame_botoes.pack(pady=10)

ctk.CTkButton(frame_botoes, text="Adicionar", command=adicionar, width=150).grid(row=0, column=0, padx=5)
ctk.CTkButton(frame_botoes, text="Limpar Tudo", command=limpar_tudo, width=150,
              fg_color="gray40", hover_color="gray30").grid(row=0, column=1, padx=5)

caixa = ctk.CTkTextbox(app, width=400, height=200)
caixa.pack(pady=10)

app.mainloop()
