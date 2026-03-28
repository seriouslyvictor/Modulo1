import customtkinter as ctk
from PIL import Image

def setup_ui(root):
    """Configura a interface do usuário"""
    # global entrada_alimento, botao_consultar, label_porcao, label_calorias, label_proteinas
    # global label_carboidratos, label_gorduras, texto_resultado, frame_carregando, label_carregando
    
    # Configurar grid principal
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(6, weight=1)
    
    # Logo
    logo_image = ctk.CTkImage(
        light_image=Image.open("foodGrader/logo.png"),
        size=(200, 200)
    )
    logo_label = ctk.CTkLabel(root, image=logo_image, text="")
    logo_label.grid(row=0, column=0, columnspan=2, pady=20)
    
    
    # Frame de entrada
    frame_entrada = ctk.CTkFrame(root)
    frame_entrada.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    frame_entrada.grid_columnconfigure(1, weight=1)
    
    # Label e entrada
    label_entrada = ctk.CTkLabel(frame_entrada, text="Nome do alimento:")
    label_entrada.grid(row=0, column=0, padx=10, pady=15, sticky="w")
    
    entrada_alimento = ctk.CTkEntry(
        frame_entrada,
        placeholder_text="Ex: BigMac, arroz, feijão...",
        font=ctk.CTkFont(size=14)
    )
    entrada_alimento.grid(row=0, column=1, padx=(10, 20), pady=15, sticky="ew")

    
    # Botão de consulta
    botao_consultar = ctk.CTkButton(
        root,
        text="🔍 Consultar",
        # command=consultar_alimento,
        font=ctk.CTkFont(size=16, weight="bold"),
        height=40,
        fg_color="#4a7c3c",
        hover_color="#3d6530"
    )
    botao_consultar.grid(row=3, column=0, columnspan=2, padx=20, pady=15, sticky="ew")
    
    # Frame de informações nutricionais
    frame_nutricao = ctk.CTkFrame(root)
    frame_nutricao.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    frame_nutricao.grid_columnconfigure([0, 1], weight=1)
    
    # Título da seção nutricional
    ctk.CTkLabel(frame_nutricao, text="📊 Informações Nutricionais", 
                font=ctk.CTkFont(size=16, weight="bold")).grid(row=0, column=0, columnspan=2, pady=(15, 10))
    
    # Label da porção (nova)
    label_porcao = ctk.CTkLabel(frame_nutricao, text="Porção: --", 
                               font=ctk.CTkFont(size=14, weight="bold"),
                               text_color="#2d5016")
    label_porcao.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
    
    # Labels de informações nutricionais
    label_calorias = ctk.CTkLabel(frame_nutricao, text="Calorias: --", 
                                 font=ctk.CTkFont(size=14))
    label_calorias.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    
    label_proteinas = ctk.CTkLabel(frame_nutricao, text="Proteínas: --",
                                  font=ctk.CTkFont(size=14))
    label_proteinas.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    
    label_carboidratos = ctk.CTkLabel(frame_nutricao, text="Carboidratos: --",
                                     font=ctk.CTkFont(size=14))
    label_carboidratos.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    
    label_gorduras = ctk.CTkLabel(frame_nutricao, text="Gorduras: --",
                                 font=ctk.CTkFont(size=14))
    label_gorduras.grid(row=3, column=1, padx=10, pady=(5, 15), sticky="w")
    
    # Frame de carregamento (inicialmente oculto)
    frame_carregando = ctk.CTkFrame(root)
    frame_carregando.grid_columnconfigure(0, weight=1)
    
    label_carregando = ctk.CTkLabel(
        frame_carregando,
        text="🔄 Consultando informações nutricionais...",
        font=ctk.CTkFont(size=14)
    )
    label_carregando.grid(row=0, column=0, pady=15)
    
    # Área de texto para observações/erros
    texto_resultado = ctk.CTkTextbox(
        root,
        height=120,
        wrap="word"
    )
    texto_resultado.grid(row=6, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="nsew")

def main():
    """Função principal da aplicação"""
    global root
    
    # Configurar aparência
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    # Criar janela principal
    root = ctk.CTk()
    root.title("Consultor Nutricional")
    root.geometry("500x600")
    
    # Configurar interface
    setup_ui(root)
    
    # Executar aplicação
    root.mainloop()

if __name__ == "__main__":
    main()