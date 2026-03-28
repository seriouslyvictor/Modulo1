import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")

def calcular():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    soma = num1 + num2
    label_resultado.configure(text=f"Resultado: {soma}")

ctk.CTkLabel(app, text="Número 1:").pack(pady=5)
entrada1 = ctk.CTkEntry(app, width=150)
entrada1.pack()

ctk.CTkLabel(app, text="Número 2:").pack(pady=5)
entrada2 = ctk.CTkEntry(app, width=150)
entrada2.pack()

ctk.CTkButton(app, text="Somar", command=calcular).pack(pady=10)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack()

app.mainloop()
