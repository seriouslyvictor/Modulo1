import customtkinter as ctk

# O CustomTkinter cuida de toda a interface visual moderna,
# mas ele NÃO tem uma janela de "abrir arquivo" embutida.
# Para isso usamos o 'filedialog', que faz parte do tkinter —
# a biblioteca original do Python que o CTK foi construído em cima.
# Ou seja: CTK é o visual bonito, tkinter é a base com as ferramentas extras.
from tkinter import filedialog

# Pillow (PIL) é a biblioteca que sabe abrir arquivos de imagem do disco.
# O CTK não abre imagens diretamente — ele depende do Pillow para fazer isso.
# Fluxo: Pillow lê o arquivo → CTkImage converte → CTkLabel exibe.
from PIL import Image

app = ctk.CTk()
app.title("⚔️ Ficha de Personagem")
app.geometry("520x680")
app.resizable(False, False)

# Variável global que guarda o caminho do arquivo de imagem escolhido.
# Começa vazia — significa que nenhuma imagem foi selecionada ainda.
# Precisamos dela no escopo global porque duas funções diferentes
# precisam acessá-la: escolher_imagem() grava, gerar_ficha() lê.
caminho_imagem = ""

# --- Título ---
ctk.CTkLabel(app, text="⚔️ Criador de Ficha Anime", font=("Arial", 20, "bold")).pack(pady=15)

# --- Formulário ---
frame_form = ctk.CTkFrame(app)
frame_form.pack(padx=20, pady=5, fill="x")

ctk.CTkLabel(frame_form, text="Nome do personagem:").grid(row=0, column=0, padx=10, pady=8, sticky="w")
entrada_nome = ctk.CTkEntry(frame_form, width=240, placeholder_text="Ex: Naruto Uzumaki")
entrada_nome.grid(row=0, column=1, padx=10, pady=8)

ctk.CTkLabel(frame_form, text="Anime de origem:").grid(row=1, column=0, padx=10, pady=8, sticky="w")
entrada_anime = ctk.CTkEntry(frame_form, width=240, placeholder_text="Ex: Naruto Shippuden")
entrada_anime.grid(row=1, column=1, padx=10, pady=8)

ctk.CTkLabel(frame_form, text="Tipo de poder:").grid(row=2, column=0, padx=10, pady=8, sticky="w")
opcao_poder = ctk.CTkOptionMenu(frame_form, values=["🔥 Fogo", "💨 Vento", "🌑 Trevas", "💧 Água", "⚡ Raio"])
opcao_poder.grid(row=2, column=1, padx=10, pady=8)

ctk.CTkLabel(frame_form, text="Nível de poder (1-9999):").grid(row=3, column=0, padx=10, pady=8, sticky="w")
entrada_nivel = ctk.CTkEntry(frame_form, width=240, placeholder_text="Ex: 9000")
entrada_nivel.grid(row=3, column=1, padx=10, pady=8)

# --- Funções ---

def escolher_imagem():
    # 'global' avisa ao Python que vamos MODIFICAR a variável caminho_imagem
    # que está fora desta função. Sem essa linha, o Python criaria uma
    # variável nova só dentro da função e jogaria fora logo em seguida —
    # e a gente perderia o caminho escolhido.
    global caminho_imagem

    # askopenfilename() abre a janela de "Abrir arquivo" do sistema operacional.
    # Ela não abre a imagem — ela só PERGUNTA ao usuário qual arquivo ele quer,
    # e devolve o caminho completo como texto. Ex: "C:/Users/aluno/foto.png"
    # O parâmetro 'filetypes' limita quais arquivos aparecem na janela,
    # filtrando apenas imagens. Sem ele, apareceriam todos os arquivos do PC.
    caminho = filedialog.askopenfilename(
        title="Escolha a imagem do personagem",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.webp")]
    )

    # Se o usuário cancelou a janela, 'caminho' fica vazio ("").
    # O 'if caminho' garante que só atualizamos se ele realmente escolheu algo.
    if caminho:
        caminho_imagem = caminho
        label_status.configure(text="🖼️ Imagem selecionada!", text_color="lightblue")


def gerar_ficha():
    # Lê os valores digitados nos campos e remove espaços das bordas com .strip()
    nome  = entrada_nome.get().strip()
    anime = entrada_anime.get().strip()
    poder = opcao_poder.get()  # OptionMenu também usa .get(), igual ao Entry

    # Validação: se nome ou anime estiverem vazios, avisa e para a função.
    # O 'return' sozinho interrompe a execução — não chega nas linhas abaixo.
    if not nome or not anime:
        label_status.configure(text="⚠️ Preencha nome e anime!", text_color="orange")
        return

    # Validação do nível: Entry sempre devolve texto, então precisamos
    # converter para int. Se o usuário digitou letra ou deixou vazio,
    # int() lança um ValueError — o try/except captura esse erro e avisa.
    try:
        nivel = int(entrada_nivel.get())
        if not 1 <= nivel <= 9999:
            raise ValueError  # força o erro se o número estiver fora do intervalo
    except ValueError:
        label_status.configure(text="⚠️ Nível deve ser um número entre 1 e 9999!", text_color="orange")
        return

    # Lógica de título: cada faixa de nível ganha um título diferente.
    # O Python testa as condições em ordem — assim que uma for verdadeira, para.
    if nivel < 500:       titulo = "🥋 Gênin"
    elif nivel < 2000:    titulo = "⚔️ Chunin"
    elif nivel < 5000:    titulo = "🗡️ Jonin"
    elif nivel < 9000:    titulo = "👑 Elite"
    else:                 titulo = "🌟 LENDÁRIO"

    # Atualiza todos os labels do card com os dados do formulário
    label_titulo_poder.configure(text=titulo)
    label_nome_card.configure(text=f"Nome: {nome}")
    label_anime_card.configure(text=f"Anime: {anime}")
    label_poder_card.configure(text=f"Poder: {poder}")
    label_nivel_card.configure(text=f"Nível: {nivel}")

    # Só tenta carregar a imagem se o usuário escolheu uma
    if caminho_imagem:
        # Pillow abre o arquivo de imagem do disco
        img_pil = Image.open(caminho_imagem)
        # CTkImage converte para um formato que o CTK entende e define o tamanho
        img_ctk = ctk.CTkImage(light_image=img_pil, size=(110, 130))
        # Atualiza o label do card para exibir a imagem
        label_img_card.configure(image=img_ctk, text="")
        # IMPORTANTE: guardamos a referência da imagem dentro do próprio label.
        # O Python descarta da memória tudo que não está sendo usado.
        # Se não fizermos isso, a imagem some da tela logo depois de aparecer.
        label_img_card.image = img_ctk

    label_status.configure(text="✅ Ficha gerada!", text_color="lightgreen")


def limpar():
    # Precisamos de 'global' aqui também porque vamos zerar caminho_imagem
    global caminho_imagem
    caminho_imagem = ""

    # .delete(0, "end") apaga todo o conteúdo de um Entry,
    # do caractere 0 até o fim ("end")
    entrada_nome.delete(0, "end")
    entrada_anime.delete(0, "end")
    entrada_nivel.delete(0, "end")

    # Volta todos os labels do card para o estado inicial
    label_titulo_poder.configure(text="— SEM TÍTULO —")
    label_nome_card.configure(text="Nome: —")
    label_anime_card.configure(text="Anime: —")
    label_poder_card.configure(text="Poder: —")
    label_nivel_card.configure(text="Nível: —")
    # image=None remove a imagem do label e o text volta a aparecer
    label_img_card.configure(image=None, text="sem\nimagem")
    label_status.configure(text="")


# --- Botões ---
botao_imagem = ctk.CTkButton(app, text="🖼️ Escolher Imagem do Personagem",
                              command=escolher_imagem, width=280, fg_color="#4a4a8a")
botao_imagem.pack(pady=8)

botao_gerar = ctk.CTkButton(app, text="⚔️ Gerar Ficha", command=gerar_ficha,
                             width=200, height=38, font=("Arial", 13, "bold"),
                             fg_color="#8b0000", hover_color="#a00000")
botao_gerar.pack(pady=5)

botao_limpar = ctk.CTkButton(app, text="Limpar", command=limpar,
                              width=200, fg_color="gray40", hover_color="gray30")
botao_limpar.pack(pady=4)

label_status = ctk.CTkLabel(app, text="")
label_status.pack()

# --- Frame do Card ---
frame_card = ctk.CTkFrame(app, fg_color="#0d0d1a", corner_radius=14)
frame_card.pack(padx=20, pady=10, fill="x")
frame_card.columnconfigure(0, weight=1)
frame_card.columnconfigure(1, weight=2)

label_img_card = ctk.CTkLabel(frame_card, text="sem\nimagem", width=110, height=130,
                               fg_color="#1a1a2e", corner_radius=8)
label_img_card.grid(row=0, column=0, rowspan=5, padx=15, pady=15, sticky="n")

label_titulo_poder = ctk.CTkLabel(frame_card, text="— SEM TÍTULO —",
                                   font=("Arial", 11, "bold"), text_color="#ffd700")
label_titulo_poder.grid(row=0, column=1, padx=10, pady=(15, 2), sticky="w")

label_nome_card  = ctk.CTkLabel(frame_card, text="Nome: —",  font=("Arial", 15, "bold"), text_color="white")
label_nome_card.grid(row=1, column=1, padx=10, pady=2, sticky="w")

label_anime_card = ctk.CTkLabel(frame_card, text="Anime: —", font=("Arial", 12), text_color="#aaaacc")
label_anime_card.grid(row=2, column=1, padx=10, pady=2, sticky="w")

label_poder_card = ctk.CTkLabel(frame_card, text="Poder: —", font=("Arial", 12), text_color="#aaaacc")
label_poder_card.grid(row=3, column=1, padx=10, pady=2, sticky="w")

label_nivel_card = ctk.CTkLabel(frame_card, text="Nível: —", font=("Arial", 12), text_color="#aaaacc")
label_nivel_card.grid(row=4, column=1, padx=10, pady=(2, 15), sticky="w")

app.mainloop()
