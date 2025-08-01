import customtkinter as ctk

#criando a tela
tela = ctk.CTk()
tela.title("Meu app")


def btn_callback():
    print("Teje apertado")

def informar_valor():
    try:
        valor = int(entrada.get().strip())
        if valor < 0:
            resultado.configure(text="Somente números positivos...")    
            return
    except ValueError:
        resultado.configure(text="Insira somente numeros...")
        return
    
    cotacao = 5.60
    valor_cotacao = valor * cotacao
    resultado.configure(text=valor_cotacao)

#widgets
botao = ctk.CTkButton(tela, text="Meu botao", command=btn_callback)
botao2 = ctk.CTkButton(tela, text="Meu otro botao", command=btn_callback)
caixa = ctk.CTkCheckBox(tela, text="Meu checkbox")


#inserindo o widget, método pack
# botao.pack()


#inserindo o widget, método place
# botao2.place(x=50, y=50)

#inserind widgets, metodo grid
botao.grid(row=0, column=0)
caixa.grid(row=0, column=1)
#este widget irá expandir para as laterais se houver espaço.
botao2.grid(row=1, column=0, sticky="ew")

#coluna 0 irá redimensionar se tiver espaço
tela.grid_columnconfigure(0, weight=1)

#Trabalhando com entries
titulo =  ctk.CTkLabel(tela, text="Conversor de Doletas", font=ctk.CTkFont(size=18, family="Arial", weight="bold"))
entrada = ctk.CTkEntry(tela, placeholder_text="Coloque um valor...", font=ctk.CTkFont(size=14, family="Arial", weight="normal"))
botao3 = ctk.CTkButton(tela, text="Converter!", command=informar_valor)
resultado = ctk.CTkLabel(tela,text="O resultado aparecerá aqui...", font=ctk.CTkFont(size=14), text_color="#999999")

titulo.grid(row=2, column=0, columnspan=2)
entrada.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20, pady=20)
botao3.grid(row=4, columnspan=2)
resultado.grid(row=5,columnspan=2)

tela.mainloop()