import customtkinter as ctk

app = ctk.CTk()
app.title("Desafio 4.6 — Cronômetro Visual")
app.geometry("400x250")

contando = False
segundos = 0

label_tempo = ctk.CTkLabel(app, text="00 segundos", font=("Arial", 36, "bold"))
label_tempo.pack(pady=40)

def contar():
    global segundos
    if contando:
        segundos += 1
        label_tempo.configure(text=f"{segundos:02d} segundos")
        app.after(1000, contar)

def iniciar():
    global contando
    contando = True
    contar()

def zerar():
    global contando, segundos
    contando = False
    segundos = 0
    label_tempo.configure(text="00 segundos")

frame_botoes = ctk.CTkFrame(app, fg_color="transparent")
frame_botoes.pack()

ctk.CTkButton(frame_botoes, text="Iniciar", command=iniciar, width=120).grid(row=0, column=0, padx=10)
ctk.CTkButton(frame_botoes, text="Zerar", command=zerar, width=120,
              fg_color="gray40", hover_color="gray30").grid(row=0, column=1, padx=10)

app.mainloop()
