import customtkinter as ctk

app = ctk.CTk()
app.title("Desafio 4.4 — Calculadora de Média")
app.geometry("400x380")

frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, fill="x")

campos = []
for i in range(1, 5):
    ctk.CTkLabel(frame, text=f"Nota {i}:").grid(row=i-1, column=0, padx=10, pady=8, sticky="w")
    entrada = ctk.CTkEntry(frame, width=150, placeholder_text="0.0")
    entrada.grid(row=i-1, column=1, padx=10, pady=8)
    campos.append(entrada)

def calcular_media():
    notas = [float(c.get()) for c in campos]
    media = sum(notas) / len(notas)
    if media >= 5:
        situacao = "✅ Aprovado"
        cor = "lightgreen"
    else:
        situacao = "❌ Reprovado"
        cor = "orange"
    label_resultado.configure(text=f"Média: {media:.1f} — {situacao}", text_color=cor)

ctk.CTkButton(app, text="Calcular Média", command=calcular_media).pack(pady=10)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack(pady=5)

app.mainloop()
