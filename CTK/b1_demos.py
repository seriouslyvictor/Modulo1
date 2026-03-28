import customtkinter as ctk

# Pillow (PIL) é a biblioteca que sabe abrir arquivos de imagem do disco.
# O CTK não lê imagens diretamente — ele depende do Pillow para isso.
# Fluxo completo: Pillow abre o arquivo → CTkImage converte → CTkLabel exibe.
from PIL import Image

# 'os' é uma biblioteca padrão do Python (não precisa instalar) que
# conversa com o sistema operacional. Aqui usamos apenas uma função dela:
# os.path.exists("arquivo") — verifica se um arquivo existe no disco
# antes de tentar abri-lo. Sem essa verificação, se o arquivo não existir,
# o programa trava com um erro. Com ela, exibimos um aviso amigável.
import os

app = ctk.CTk()
app.title("Bloco 1 — Demo de Widgets e Layout")
app.geometry("520x820")

# ─────────────────────────────────────────
# Widget 1 — CTkLabel
# Serve para exibir texto fixo na tela.
# O parâmetro 'text' define o que aparece.
# 'font' recebe uma tupla: (família, tamanho, estilo)
# ─────────────────────────────────────────
ctk.CTkLabel(app, text="── Widget 1: CTkLabel ──", font=("Arial", 12, "bold")).pack(pady=(20, 2))

label = ctk.CTkLabel(app, text="Olá, turma!")
label.pack()

# ─────────────────────────────────────────
# Widget 2 — CTkButton
# Cria um botão clicável. Sem 'command=', ele não faz nada ao clicar —
# é só visual. No Bloco 2 veremos como conectar uma função a ele.
# ─────────────────────────────────────────
ctk.CTkLabel(app, text="── Widget 2: CTkButton ──", font=("Arial", 12, "bold")).pack(pady=(15, 2))

botao = ctk.CTkButton(app, text="Clique aqui")
botao.pack()

# ─────────────────────────────────────────
# Widget 3 — CTkEntry
# Campo de uma linha onde o usuário digita texto.
# 'placeholder_text' é o texto cinza que aparece quando o campo está vazio —
# ele some automaticamente quando o usuário começa a digitar.
# Para ler o que foi digitado: entrada.get()  (veremos no Bloco 2)
# ─────────────────────────────────────────
ctk.CTkLabel(app, text="── Widget 3: CTkEntry ──", font=("Arial", 12, "bold")).pack(pady=(15, 2))

entrada = ctk.CTkEntry(app, placeholder_text="Digite seu nome...")
entrada.pack()

# ─────────────────────────────────────────
# Widget 4 — CTkFrame
# Um frame é uma "caixa invisível" dentro da janela.
# Ele não exibe nada sozinho — serve para agrupar outros widgets.
# Isso ajuda a organizar o layout: widgets dentro do frame
# se movem juntos e ficam visualmente separados dos outros.
# Repare: o CTkLabel abaixo usa 'moldura' como pai, não 'app'.
# ─────────────────────────────────────────
ctk.CTkLabel(app, text="── Widget 4: CTkFrame ──", font=("Arial", 12, "bold")).pack(pady=(15, 2))

moldura = ctk.CTkFrame(app)
moldura.pack(padx=20, fill="x")

ctk.CTkLabel(moldura, text="Estou dentro do frame!").pack(pady=8)

# ─────────────────────────────────────────
# Widget 5 — CTkTextbox
# Área de texto com várias linhas — diferente do Entry que é só uma.
# Útil para exibir ou receber textos longos.
# insert("0.0", texto) coloca texto na posição linha 0, coluna 0 (o início).
# Para apagar tudo: caixa.delete("0.0", "end")
# Para ler tudo: caixa.get("0.0", "end")
# ─────────────────────────────────────────
ctk.CTkLabel(app, text="── Widget 5: CTkTextbox ──", font=("Arial", 12, "bold")).pack(pady=(15, 2))

caixa = ctk.CTkTextbox(app, width=380, height=60)
caixa.pack()
caixa.insert("0.0", "Aqui cabe muito texto...")

# ─────────────────────────────────────────
# Widget 6 — CTkImage + CTkLabel
# O CTK não exibe imagens diretamente. O processo tem 3 etapas:
#   1. Pillow abre o arquivo do disco → objeto Image
#   2. CTkImage converte para formato CTK e define o tamanho na tela
#   3. CTkLabel recebe a imagem e a exibe (text="" para não aparecer texto junto)
#
# Antes de tentar abrir, usamos os.path.exists() para verificar se o
# arquivo realmente existe. Tentar abrir um arquivo que não existe
# causa um erro e fecha o programa — o if/else aqui evita isso.
# ─────────────────────────────────────────
ctk.CTkLabel(app, text="── Widget 6: CTkImage ──", font=("Arial", 12, "bold")).pack(pady=(15, 2))

if os.path.exists("logo.png"):
    # Passo 1: Pillow lê o arquivo de imagem do disco
    imagem_pil = Image.open("logo.png")
    # Passo 2: CTkImage converte e define o tamanho de exibição (não altera o arquivo)
    imagem_ctk = ctk.CTkImage(light_image=imagem_pil, size=(80, 80))
    # Passo 3: CTkLabel exibe — image= recebe a imagem, text="" esconde o texto padrão
    label_logo = ctk.CTkLabel(app, image=imagem_ctk, text="")
    label_logo.pack()
    ctk.CTkLabel(app, text="Minha Escola", font=("Arial", 14, "bold")).pack()
else:
    # Se o arquivo não existe, mostra um aviso ao invés de travar
    ctk.CTkLabel(app, text="⚠️ Coloque um arquivo logo.png nesta pasta para ver a imagem",
                 text_color="orange").pack()

# ─────────────────────────────────────────
# Layout — grid (posicionamento em tabela)
# pack() empilha widgets um embaixo do outro — simples, mas sem controle fino.
# grid() posiciona em linhas (row) e colunas (column), como uma planilha.
# É ideal para formulários onde Labels ficam à esquerda e Entrys à direita.
#
# sticky="w" alinha o widget à esquerda dentro da célula (w = west = oeste).
# padx/pady adicionam espaço ao redor do widget dentro da célula.
#
# ⚠️ Regra importante: nunca misture pack() e grid() no mesmo container.
# Aqui usamos pack() na janela principal e grid() dentro do frame_grid.
# ─────────────────────────────────────────
ctk.CTkLabel(app, text="── Layout: grid (formulário) ──", font=("Arial", 12, "bold")).pack(pady=(15, 2))

frame_grid = ctk.CTkFrame(app)
frame_grid.pack(padx=20, fill="x")

ctk.CTkLabel(frame_grid, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
ctk.CTkEntry(frame_grid).grid(row=0, column=1, padx=10, pady=5)

ctk.CTkLabel(frame_grid, text="Idade:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
ctk.CTkEntry(frame_grid).grid(row=1, column=1, padx=10, pady=5)

app.mainloop()
