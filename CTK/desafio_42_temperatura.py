import customtkinter as ctk

app = ctk.CTk()
app.title("Desafio 4.2 — Conversor de Temperatura")
app.geometry("400x250")

ctk.CTkLabel(app, text="Temperatura em Celsius:").pack(pady=10)

entrada_celsius = ctk.CTkEntry(app, width=200, placeholder_text="Ex: 25")
entrada_celsius.pack(pady=5)

def converter():
    celsius = float(entrada_celsius.get())
    fahrenheit = celsius * 1.8 + 32
    label_resultado.configure(text=f"{celsius}°C = {fahrenheit:.1f}°F")

ctk.CTkButton(app, text="Converter", command=converter).pack(pady=10)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack(pady=5)

app.mainloop()
