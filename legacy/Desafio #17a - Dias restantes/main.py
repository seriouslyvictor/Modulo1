import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()

class FontStyles:
    # Fontes de títulos
    TITULO = ctk.CTkFont(family="Arial", size=20, weight="bold")
    SUBTITULO = ctk.CTkFont(family="Arial", size=16, weight="bold")
    CORPO = ctk.CTkFont(family="Arial", size=14, weight="bold")



def calcular_dias():
    """Calcula quantos dias uma criatura já viveu"""
    try:
        idade_atual = idade_entry.get().strip()

        if not idade_atual:
            mostrar_resultado("Por favor, digite sua idade")
        idade_atual =  int(idade_atual)

        if idade_atual < 0:
            mostrar_resultado("Idade não pode ser negativa.")
        elif idade_atual > 150:
            mostrar_resultado("Insira uma idade realista!")

        dias_vividos = int(idade_atual * 365.25)
        texto_resultado = f"Você já viveu aproximadamente {dias_vividos} dias! Impressionante!"
        mostrar_resultado(texto_resultado)
        
    except ValueError:
        mostrar_resultado("Apenas números.")
        

def mostrar_resultado(valor):
    resultado_label.configure(text=valor, text_color="white")



root.title("Calculadora de dias vividos")
root.geometry("400x300")

root.grid_columnconfigure(0, weight=1)

titulo_label = ctk.CTkLabel(root, text="Calculadora de dias!", font=FontStyles.TITULO)
titulo_label.grid(row=0, column=0, pady=20, sticky="ew")

entrada_frame = ctk.CTkFrame(root, fg_color="#333")
entrada_frame.grid(column=0, row=1, padx=20, pady=10, sticky='ew')
entrada_frame.grid_columnconfigure(1, weight=1)

#inputs começam aqui, no frame apropriado
idade_label = ctk.CTkLabel(entrada_frame, text="Sua idade em anos:", font=FontStyles.CORPO)
idade_label.grid(column=0, row=0, padx=10, pady=15, sticky="ew")
idade_entry = ctk.CTkEntry(entrada_frame)
idade_entry.grid(column=1, row=0, padx=(10,20), pady=15, sticky="ew")
botao_calc = ctk.CTkButton(root, text="Calcular!", command=calcular_dias, height=40)

botao_calc.grid(column=0, row=2, columnspan=2, sticky="ew", padx=20)


resultado_frame = ctk.CTkFrame(root, fg_color="#333")
resultado_frame.grid(column=0, row=3, padx=20, pady=(10,20), sticky="nsew")
resultado_frame.grid_columnconfigure(0, weight=1)
resultado_frame.grid_rowconfigure(0, weight=1)

resultado_label = ctk.CTkLabel(resultado_frame, text="O resultado aparecerá aqui.", wraplength=300)
resultado_label.grid(row=0, column=0, padx=20, pady=15, sticky="nsew")


root.mainloop()