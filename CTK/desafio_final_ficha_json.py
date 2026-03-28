import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import json
import os

app = ctk.CTk()
app.title("⚔️ Ficha de Personagem — Com Memória")
app.geometry("520x720")
app.resizable(False, False)

ARQUIVO = "ficha.json"
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

label_status = ctk.CTkLabel(app, text="")
label_status.pack(pady=4)

# --- Funções auxiliares ---
def _aplicar_imagem(caminho):
    """Carrega uma imagem do caminho e aplica no card. Retorna True se deu certo."""
    if caminho and os.path.exists(caminho):
        img_pil = Image.open(caminho)
        img_ctk = ctk.CTkImage(light_image=img_pil, size=(110, 130))
        label_img_card.configure(image=img_ctk, text="")
        label_img_card.image = img_ctk
        return True
    return False

def _titulo_por_nivel(nivel):
    if nivel < 500:    return "🥋 Gênin"
    elif nivel < 2000: return "⚔️ Chunin"
    elif nivel < 5000: return "🗡️ Jonin"
    elif nivel < 9000: return "👑 Elite"
    else:              return "🌟 LENDÁRIO"

# --- Funções principais ---
def escolher_imagem():
    global caminho_imagem
    caminho = filedialog.askopenfilename(
        title="Escolha a imagem do personagem",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.webp")]
    )
    if caminho:
        caminho_imagem = caminho
        label_status.configure(text="🖼️ Imagem selecionada!", text_color="lightblue")

def gerar_ficha():
    nome  = entrada_nome.get().strip()
    anime = entrada_anime.get().strip()
    poder = opcao_poder.get()
    if not nome or not anime:
        label_status.configure(text="⚠️ Preencha nome e anime!", text_color="orange")
        return
    try:
        nivel = int(entrada_nivel.get())
        if not 1 <= nivel <= 9999:
            raise ValueError
    except ValueError:
        label_status.configure(text="⚠️ Nível deve ser um número entre 1 e 9999!", text_color="orange")
        return

    label_titulo_poder.configure(text=_titulo_por_nivel(nivel))
    label_nome_card.configure(text=f"Nome: {nome}")
    label_anime_card.configure(text=f"Anime: {anime}")
    label_poder_card.configure(text=f"Poder: {poder}")
    label_nivel_card.configure(text=f"Nível: {nivel}")
    _aplicar_imagem(caminho_imagem)
    label_status.configure(text="✅ Ficha gerada!", text_color="lightgreen")

def salvar():
    nome  = entrada_nome.get().strip()
    anime = entrada_anime.get().strip()
    if not nome or not anime:
        label_status.configure(text="⚠️ Preencha os campos antes de salvar!", text_color="orange")
        return
    try:
        nivel = int(entrada_nivel.get())
    except ValueError:
        label_status.configure(text="⚠️ Nível inválido!", text_color="orange")
        return

    dados = {
        "nome":   nome,
        "anime":  anime,
        "poder":  opcao_poder.get(),
        "nivel":  nivel,
        "imagem": caminho_imagem   # salva o caminho, não a imagem em si
    }
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    label_status.configure(text=f"💾 Ficha salva em {ARQUIVO}!", text_color="lightblue")

def carregar():
    global caminho_imagem
    if not os.path.exists(ARQUIVO):
        label_status.configure(text="⚠️ Nenhuma ficha salva encontrada.", text_color="orange")
        return

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    entrada_nome.delete(0, "end")
    entrada_nome.insert(0, dados.get("nome", ""))
    entrada_anime.delete(0, "end")
    entrada_anime.insert(0, dados.get("anime", ""))
    entrada_nivel.delete(0, "end")
    entrada_nivel.insert(0, str(dados.get("nivel", "")))
    opcao_poder.set(dados.get("poder", "🔥 Fogo"))

    caminho_imagem = dados.get("imagem", "")
    if caminho_imagem and not _aplicar_imagem(caminho_imagem):
        label_status.configure(text="📂 Ficha carregada! (imagem não encontrada)", text_color="orange")
    else:
        label_status.configure(text="📂 Ficha carregada com sucesso!", text_color="lightgreen")

    nivel = dados.get("nivel", 0)
    label_titulo_poder.configure(text=_titulo_por_nivel(nivel))
    label_nome_card.configure(text=f"Nome: {dados.get('nome', '—')}")
    label_anime_card.configure(text=f"Anime: {dados.get('anime', '—')}")
    label_poder_card.configure(text=f"Poder: {dados.get('poder', '—')}")
    label_nivel_card.configure(text=f"Nível: {nivel}")

# --- Botões ---
botao_imagem = ctk.CTkButton(app, text="🖼️ Escolher Imagem",
                              command=escolher_imagem, width=200, fg_color="#4a4a8a")
botao_imagem.pack(pady=4)

frame_botoes = ctk.CTkFrame(app, fg_color="transparent")
frame_botoes.pack(pady=6)

ctk.CTkButton(frame_botoes, text="⚔️ Gerar",    command=gerar_ficha, width=120,
              fg_color="#8b0000", hover_color="#a00000").grid(row=0, column=0, padx=5)
ctk.CTkButton(frame_botoes, text="💾 Salvar",    command=salvar,      width=120,
              fg_color="#2d6a4f").grid(row=0, column=1, padx=5)
ctk.CTkButton(frame_botoes, text="📂 Carregar",  command=carregar,    width=120,
              fg_color="#1d3557").grid(row=0, column=2, padx=5)

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
