# 🖥️ Plano de Aula — Interfaces Gráficas com Python e CustomTkinter
**Duração total:** 6 horas | **Público:** Ensino médio público, adolescentes | **Pré-requisito:** `def` e `return` básicos

---

## Visão Geral da Aula

| Bloco | Tema | Duração |
|---|---|---|
| 1 | Visão Geral: Widgets, Imagens e Layout | 1h15 |
| 2 | Fazendo a Interface "Fazer Algo" | 1h |
| 3 | Construindo o Gerador de Carteirinha | 1h30 |
| 4 | Desafios Progressivos | 2h |
| 5 | Desafio Final com JSON | 30min |

---

## Antes de Começar

### Instalação
```bash
pip install customtkinter
```

### Código mínimo de referência (sempre visível na lousa)
```python
import customtkinter as ctk

app = ctk.CTk()
app.title("Meu Programa")
app.geometry("400x300")

# widgets vão aqui

app.mainloop()
```

> 💡 **Dica para o professor:** Mantenha esse código base colado no quadro/projetor o tempo todo. Os alunos voltarão a ele constantemente.

---

## BLOCO 1 — Visão Geral: Widgets e Layout (1h)

### Objetivo
O aluno consegue identificar os principais widgets e posicioná-los na tela usando `pack` e `grid`.

---

### 1.1 O que é um Widget?
> "Widget é qualquer coisa que aparece na janela. Botão, caixa de texto, rótulo — tudo é widget."

Apresente cada widget com um exemplo ao vivo. Cole o código, rode, mostre o resultado.

---

#### Widget 1 — `CTkLabel` (rótulo de texto)
```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x200")

label = ctk.CTkLabel(app, text="Olá, turma!")
label.pack(pady=20)

app.mainloop()
```

---

#### Widget 2 — `CTkButton` (botão)
```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x200")

botao = ctk.CTkButton(app, text="Clique aqui")
botao.pack(pady=20)

app.mainloop()
```

---

#### Widget 3 — `CTkEntry` (caixa de texto para o usuário digitar)
```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x200")

entrada = ctk.CTkEntry(app, placeholder_text="Digite seu nome...")
entrada.pack(pady=20)

app.mainloop()
```

---

#### Widget 4 — `CTkFrame` (moldura / divisória)
```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")

moldura = ctk.CTkFrame(app)
moldura.pack(pady=20, padx=20, fill="both")

label_dentro = ctk.CTkLabel(moldura, text="Estou dentro do frame!")
label_dentro.pack(pady=10)

app.mainloop()
```

> 💡 **Explique:** "O Frame é como uma caixa dentro da janela. Ajuda a organizar os outros widgets."

---

#### Widget 5 — `CTkTextbox` (área de texto maior)
```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")

caixa = ctk.CTkTextbox(app, width=300, height=150)
caixa.pack(pady=20)
caixa.insert("0.0", "Aqui cabe muito texto...")

app.mainloop()
```

---

#### Widget 6 — Imagens com `CTkImage` + `CTkLabel`

> "O CustomTkinter não exibe imagens diretamente — a gente carrega a imagem com a biblioteca **Pillow** e entrega para um Label exibir."

**Instalação necessária (só uma vez):**
```bash
pip install pillow
```

**Exemplo básico — exibir uma imagem:**
```python
import customtkinter as ctk
from PIL import Image

app = ctk.CTk()
app.geometry("400x300")

# 1. Carrega a imagem do disco
imagem_pil = Image.open("foto.png")

# 2. Converte para o formato que o CTK entende
imagem_ctk = ctk.CTkImage(light_image=imagem_pil, size=(150, 150))

# 3. Coloca dentro de um Label (com text="" para não aparecer texto)
label_imagem = ctk.CTkLabel(app, image=imagem_ctk, text="")
label_imagem.pack(pady=20)

app.mainloop()
```

> 💡 **Explique:** "O arquivo `foto.png` precisa estar na **mesma pasta** do seu código Python. Se estiver em outro lugar, dá erro."

---

**Exemplo com imagem + texto embaixo (estilo logo + título):**
```python
import customtkinter as ctk
from PIL import Image

app = ctk.CTk()
app.geometry("400x300")

imagem_pil = Image.open("logo.png")
imagem_ctk = ctk.CTkImage(light_image=imagem_pil, size=(100, 100))

label_logo = ctk.CTkLabel(app, image=imagem_ctk, text="")
label_logo.pack(pady=(20, 5))

label_titulo = ctk.CTkLabel(app, text="Minha Escola", font=("Arial", 18, "bold"))
label_titulo.pack()

app.mainloop()
```

> 💡 **Dica sobre tamanho:** o parâmetro `size=(largura, altura)` redimensiona a imagem automaticamente. Não precisa editar o arquivo original.

> ⚠️ **Atenção:** mantenha a variável `imagem_ctk` fora de funções (em escopo global ou de janela). Se ela for criada dentro de uma função e não for referenciada em nenhum lugar, o Python pode descartá-la da memória e a imagem some da tela.

---

### 🎯 Mini-Desafio 1D — Logo do App *(~10 min)*

> Salve qualquer imagem (foto, logo, ícone) na pasta do seu código com o nome `logo.png`.
> Crie uma janela que exibe:
> - A imagem com tamanho `(120, 120)`
> - Abaixo dela, um Label com o texto **"Meu Primeiro App com Imagem"**
>
> ✅ Critério: a imagem aparece na janela, sem erro, com o texto abaixo.
>
> 💡 Não tem imagem disponível? Use o Paint ou baixe qualquer `.png` da internet e renomeie para `logo.png`.

---

### 1.2 Como posicionar widgets — `pack` vs `grid`

#### Método `pack` — simples, empilha um embaixo do outro
```python
label1 = ctk.CTkLabel(app, text="Primeiro")
label1.pack()

label2 = ctk.CTkLabel(app, text="Segundo")
label2.pack()
```

Parâmetros úteis do `pack`:
- `pady=10` → espaço vertical
- `padx=10` → espaço horizontal
- `fill="x"` → estica horizontalmente
- `side="left"` / `side="right"` → coloca lado a lado

---

#### Método `grid` — posiciona em linhas e colunas (como uma tabela)
```python
label_nome = ctk.CTkLabel(app, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)

entrada_nome = ctk.CTkEntry(app)
entrada_nome.grid(row=0, column=1, padx=10, pady=5)

label_idade = ctk.CTkLabel(app, text="Idade:")
label_idade.grid(row=1, column=0, padx=10, pady=5)

entrada_idade = ctk.CTkEntry(app)
entrada_idade.grid(row=1, column=1, padx=10, pady=5)
```

> ⚠️ **Regra importante:** nunca misture `pack` e `grid` na mesma janela (ou no mesmo frame). Escolha um para cada janela.

---

### 🎯 Mini-Desafios do Bloco 1

> **Instrução para o professor:** Após mostrar os exemplos acima, dê 5–10 minutos para cada desafio. Não dê a resposta imediatamente — deixe o aluno tentar. Circule pela sala.

---

**Mini-Desafio 1A — Label e Button** *(~5 min)*
> Crie uma janela com:
> - Um label escrito **"Bem-vindo ao meu app!"**
> - Um botão escrito **"Entrar"**
>
> ✅ Critério: os dois aparecem na janela sem erro.

---

**Mini-Desafio 1B — Formulário com grid** *(~10 min)*
> Crie uma janelinha com três campos usando `grid`:
> - Nome
> - Turma
> - Número de matrícula
>
> Cada campo tem um Label à esquerda e um Entry à direita.
>
> ✅ Critério: os três campos aparecem alinhados, um embaixo do outro.

---

**Mini-Desafio 1C — Frame colorido** *(~5 min)*
> Crie uma janela com dois Frames lado a lado (use `side="left"` no `pack`).
> Dentro de cada frame coloque um Label com um texto diferente.
>
> ✅ Critério: dois frames visíveis, cada um com seu texto.

---

## BLOCO 2 — Fazendo a Interface "Fazer Algo" (1h)

### Objetivo
O aluno consegue conectar um botão a uma função e atualizar elementos da tela com o resultado.

---

### 2.1 O conceito de "comando"

> "Um botão sem `command` é uma decoração. Com `command`, ele executa uma função quando clicado."

#### Estrutura básica: botão → função → resultado na tela
```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x200")

def saudar():
    label_resultado.configure(text="Olá! Botão funcionou!")

botao = ctk.CTkButton(app, text="Clique", command=saudar)
botao.pack(pady=10)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack(pady=10)

app.mainloop()
```

> 💡 **Explique a sequência:** Usuário clica → Python chama `saudar()` → `configure` atualiza o Label.

---

### 2.2 Lendo o que o usuário digitou — `.get()`

```python
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x250")

def mostrar_nome():
    nome = entrada_nome.get()
    label_resultado.configure(text=f"Seu nome é: {nome}")

label = ctk.CTkLabel(app, text="Digite seu nome:")
label.pack(pady=5)

entrada_nome = ctk.CTkEntry(app, width=200)
entrada_nome.pack(pady=5)

botao = ctk.CTkButton(app, text="Confirmar", command=mostrar_nome)
botao.pack(pady=10)

label_resultado = ctk.CTkLabel(app, text="")
label_resultado.pack(pady=5)

app.mainloop()
```

---

### 2.3 Usando variáveis para fazer cálculos

```python
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
```

> 💡 **Atenção ao `float()`:** "O Entry sempre devolve texto. Se vamos fazer conta, precisamos converter para número."

---

### 🎯 Mini-Desafios do Bloco 2

---

**Mini-Desafio 2A — Botão que muda texto** *(~5 min)*
> Crie uma janela com um botão "Revelar" e um Label que começa com `"???"`.
> Quando o botão for clicado, o Label deve mostrar seu nome completo.
>
> ✅ Critério: o label muda ao clicar no botão.

---

**Mini-Desafio 2B — Repetidor de nome** *(~10 min)*
> Crie um programa com:
> - Um Entry para o usuário digitar qualquer coisa
> - Um botão "Repetir"
> - Um Label que exibe exatamente o que foi digitado
>
> ✅ Critério: o label mostra o conteúdo do Entry ao clicar.

---

**Mini-Desafio 2C — Calculadora de dobro** *(~10 min)*
> Crie um programa que:
> - Tem um Entry para o usuário digitar um número
> - Tem um botão "Calcular Dobro"
> - Mostra o resultado em um Label (ex: `"O dobro de 5 é 10"`)
>
> ✅ Critério: o cálculo funciona corretamente.

---

**Mini-Desafio 2D — Contador de cliques** *(~10 min — desafio!)*
> Crie um programa com:
> - Um Label mostrando `"Cliques: 0"`
> - Um botão "Clicar"
> - Cada clique aumenta o número em 1
>
> 💡 Dica: você vai precisar de uma variável **fora** da função para guardar o valor atual.
>
> ✅ Critério: o número aumenta a cada clique.

---

## BLOCO 3 — Construindo a Ficha de Personagem Anime (1h30)

### Objetivo
O aluno acompanha a construção de um programa completo, entendendo como os conceitos se conectam em um projeto real — incluindo imagens e seletor de arquivo.

### O programa
O **Gerador de Ficha de Personagem Anime** recebe nome, anime, tipo de poder e nível (1–9999), permite escolher uma imagem do personagem, e exibe um card formatado na tela com barra de poder e título automático por nível.

> 💡 **Dica para o professor:** Peça para os alunos já deixarem uma imagem `.png` ou `.jpg` salva na área de trabalho antes de começar este bloco. Pode ser qualquer coisa — print de anime, foto, ícone.

---

### Passo 1 — Montar a janela base (10 min)

> **Diga para a turma:** "Sempre o mesmo começo. Estrutura mínima primeiro, a gente vai preenchendo."

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("⚔️ Ficha de Personagem")
app.geometry("520x680")
app.resizable(False, False)

app.mainloop()
```

▶ Rode. Janela vazia aparece. Confirme que todos chegaram aqui.

---

### Passo 2 — Formulário de dados (20 min)

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("⚔️ Ficha de Personagem")
app.geometry("520x680")
app.resizable(False, False)

# --- Título ---
ctk.CTkLabel(app, text="⚔️ Criador de Ficha Anime", font=("Arial", 20, "bold")).pack(pady=15)

# --- Frame do formulário ---
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

app.mainloop()
```

▶ Rode. Mostre o OptionMenu funcionando. Explique que `.get()` funciona igual ao Entry.

---

### Passo 3 — Botão para escolher imagem (15 min)

> "Agora vem algo novo: abrir uma janelinha para o usuário escolher um arquivo do computador. Isso se chama `filedialog`."

```python
# Adicione este import no topo, junto com os outros
from tkinter import filedialog

# Variável global que guarda o caminho da imagem escolhida
caminho_imagem = ""

def escolher_imagem():
    global caminho_imagem
    # Abre o explorador de arquivos, filtrando só imagens
    caminho = filedialog.askopenfilename(
        title="Escolha a imagem do personagem",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg")]
    )
    if caminho:  # só atualiza se o usuário escolheu algo (não cancelou)
        caminho_imagem = caminho
        label_status.configure(text=f"🖼️ Imagem selecionada!", text_color="lightblue")
```

```python
# Adicione o botão abaixo do frame_form
botao_imagem = ctk.CTkButton(app, text="🖼️ Escolher Imagem do Personagem",
                              command=escolher_imagem, width=280, fg_color="#4a4a8a")
botao_imagem.pack(pady=8)

label_status = ctk.CTkLabel(app, text="")
label_status.pack()
```

▶ Rode. Clique no botão e mostre a janela de seleção de arquivo abrindo. Selecione uma imagem qualquer. Mostre o status mudando.

> 💡 **Explique:** "O `filedialog` não abre a imagem — ele só nos dá o **caminho** (endereço) de onde ela está no computador. Quem abre de verdade é o Pillow, mais tarde."

> ⚠️ **Atenção ao `global`:** "Precisamos de `global caminho_imagem` porque queremos que a função *modifique* uma variável que está fora dela. Sem o `global`, o Python criaria uma variável nova só dentro da função e jogaria fora em seguida."

---

### Passo 4 — Card da ficha + função gerar (20 min)

Primeiro, crie a área do card (ainda vazia):

```python
# Adicione antes do app.mainloop()

# --- Frame do Card ---
frame_card = ctk.CTkFrame(app, fg_color="#0d0d1a", corner_radius=14)
frame_card.pack(padx=20, pady=10, fill="x")

# Coluna da imagem (esquerda) e coluna dos dados (direita)
frame_card.columnconfigure(0, weight=1)
frame_card.columnconfigure(1, weight=2)

# Imagem do personagem
label_img_card = ctk.CTkLabel(frame_card, text="sem\nimagem", width=110, height=130,
                               fg_color="#1a1a2e", corner_radius=8)
label_img_card.grid(row=0, column=0, rowspan=5, padx=15, pady=15, sticky="n")

# Dados do personagem
label_titulo_poder = ctk.CTkLabel(frame_card, text="— SEM TÍTULO —",
                                   font=("Arial", 11, "bold"), text_color="#ffd700")
label_titulo_poder.grid(row=0, column=1, padx=10, pady=(15, 2), sticky="w")

label_nome_card = ctk.CTkLabel(frame_card, text="Nome: —",
                                font=("Arial", 15, "bold"), text_color="white")
label_nome_card.grid(row=1, column=1, padx=10, pady=2, sticky="w")

label_anime_card = ctk.CTkLabel(frame_card, text="Anime: —",
                                 font=("Arial", 12), text_color="#aaaacc")
label_anime_card.grid(row=2, column=1, padx=10, pady=2, sticky="w")

label_poder_card = ctk.CTkLabel(frame_card, text="Poder: —",
                                 font=("Arial", 12), text_color="#aaaacc")
label_poder_card.grid(row=3, column=1, padx=10, pady=2, sticky="w")

label_nivel_card = ctk.CTkLabel(frame_card, text="Nível: —",
                                 font=("Arial", 12), text_color="#aaaacc")
label_nivel_card.grid(row=4, column=1, padx=10, pady=(2, 15), sticky="w")
```

Agora a função `gerar_ficha()` com a lógica de título e imagem:

```python
from PIL import Image  # adicione este import no topo

def gerar_ficha():
    nome  = entrada_nome.get().strip()
    anime = entrada_anime.get().strip()
    poder = opcao_poder.get()

    # Validação
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

    # Título automático baseado no nível
    if nivel < 500:
        titulo = "🥋 Gênin"
    elif nivel < 2000:
        titulo = "⚔️ Chunin"
    elif nivel < 5000:
        titulo = "🗡️ Jonin"
    elif nivel < 9000:
        titulo = "👑 Elite"
    else:
        titulo = "🌟 LENDÁRIO"

    # Atualiza os labels do card
    label_titulo_poder.configure(text=titulo)
    label_nome_card.configure(text=f"Nome: {nome}")
    label_anime_card.configure(text=f"Anime: {anime}")
    label_poder_card.configure(text=f"Poder: {poder}")
    label_nivel_card.configure(text=f"Nível: {nivel}")

    # Exibe a imagem se foi escolhida
    if caminho_imagem:
        img_pil = Image.open(caminho_imagem)
        img_ctk = ctk.CTkImage(light_image=img_pil, size=(110, 130))
        label_img_card.configure(image=img_ctk, text="")
        label_img_card.image = img_ctk  # mantém referência para não sumir

    label_status.configure(text="✅ Ficha gerada!", text_color="lightgreen")
```

> 💡 **Explique o `label_img_card.image = img_ctk`:** "Essa linha parece estranha, mas é necessária. O Python automaticamente apaga da memória variáveis que ninguém está usando. Guardando a imagem dentro do próprio label, garantimos que ela não vai desaparecer."

```python
# Adicione o botão Gerar logo acima do label_status
botao_gerar = ctk.CTkButton(app, text="⚔️ Gerar Ficha", command=gerar_ficha,
                             width=200, height=38, font=("Arial", 13, "bold"),
                             fg_color="#8b0000", hover_color="#a00000")
botao_gerar.pack(pady=5)
```

▶ Rode. Preencha os campos, escolha uma imagem, clique em Gerar. Mostre o card completo. Teste diferentes níveis para ver os títulos mudando.

---

### Passo 5 — Botão Limpar (10 min)

```python
def limpar():
    global caminho_imagem
    caminho_imagem = ""
    entrada_nome.delete(0, "end")
    entrada_anime.delete(0, "end")
    entrada_nivel.delete(0, "end")
    label_titulo_poder.configure(text="— SEM TÍTULO —")
    label_nome_card.configure(text="Nome: —")
    label_anime_card.configure(text="Anime: —")
    label_poder_card.configure(text="Poder: —")
    label_nivel_card.configure(text="Nível: —")
    label_img_card.configure(image=None, text="sem\nimagem")
    label_status.configure(text="")

botao_limpar = ctk.CTkButton(app, text="Limpar", command=limpar,
                              width=200, fg_color="gray40", hover_color="gray30")
botao_limpar.pack(pady=4)
```

▶ Teste o fluxo completo: preencher → escolher imagem → gerar → limpar → repetir.

---

### Código Final Completo do Bloco 3

```python
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image

app = ctk.CTk()
app.title("⚔️ Ficha de Personagem")
app.geometry("520x680")
app.resizable(False, False)

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
    global caminho_imagem
    caminho = filedialog.askopenfilename(
        title="Escolha a imagem do personagem",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg")]
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

    if nivel < 500:       titulo = "🥋 Gênin"
    elif nivel < 2000:    titulo = "⚔️ Chunin"
    elif nivel < 5000:    titulo = "🗡️ Jonin"
    elif nivel < 9000:    titulo = "👑 Elite"
    else:                 titulo = "🌟 LENDÁRIO"

    label_titulo_poder.configure(text=titulo)
    label_nome_card.configure(text=f"Nome: {nome}")
    label_anime_card.configure(text=f"Anime: {anime}")
    label_poder_card.configure(text=f"Poder: {poder}")
    label_nivel_card.configure(text=f"Nível: {nivel}")

    if caminho_imagem:
        img_pil = Image.open(caminho_imagem)
        img_ctk = ctk.CTkImage(light_image=img_pil, size=(110, 130))
        label_img_card.configure(image=img_ctk, text="")
        label_img_card.image = img_ctk

    label_status.configure(text="✅ Ficha gerada!", text_color="lightgreen")

def limpar():
    global caminho_imagem
    caminho_imagem = ""
    entrada_nome.delete(0, "end")
    entrada_anime.delete(0, "end")
    entrada_nivel.delete(0, "end")
    label_titulo_poder.configure(text="— SEM TÍTULO —")
    label_nome_card.configure(text="Nome: —")
    label_anime_card.configure(text="Anime: —")
    label_poder_card.configure(text="Poder: —")
    label_nivel_card.configure(text="Nível: —")
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
```

---

## BLOCO 4 — Desafios Progressivos (2h)

### Instrução para o professor
> Os alunos trabalham sozinhos ou em dupla. Você circula, orienta, mas **não entrega o código pronto**. Incentive tentativas, mesmo que erradas. Um aluno que tenta e erra aprende mais do que um que copia.
>
> Os 3 primeiros desafios são **quase triviais** de propósito — para garantir a primeira vitória rápida.

---

### ⭐ Nível 1 — Vitórias Rápidas

---

**Desafio 4.1 — Tag de Nome** *(~10 min)*

> Crie uma janela simples. O usuário digita o nome e clica em "Criar Tag".
> O resultado mostrado deve ser: `"Olá! Meu nome é [nome digitado] 👋"`

✅ Foco: `.get()` + `.configure()` + `command`

---

**Desafio 4.2 — Conversor de Temperatura** *(~15 min)*

> Crie um programa que converte Celsius para Fahrenheit.
> Fórmula: `F = C * 1.8 + 32`
>
> - Entry para o usuário digitar os graus em Celsius
> - Botão "Converter"
> - Label mostrando o resultado: `"25°C = 77.0°F"`

✅ Foco: converter string para float, fazer cálculo, exibir resultado formatado

---

**Desafio 4.3 — Verificador de Senha** *(~15 min)*

> Crie um app com dois campos: "Digite a senha" e "Confirme a senha".
> Ao clicar em "Verificar":
> - Se as senhas forem iguais: label fica verde com `"✅ Senhas iguais!"`
> - Se forem diferentes: label fica vermelho/laranja com `"❌ Senhas diferentes!"`

✅ Foco: comparar strings, mudar `text_color` do label

---

### ⭐⭐ Nível 2 — Aplicando Lógica

---

**Desafio 4.4 — Calculadora de Média** *(~20 min)*

> Crie um programa com 4 campos (Nota 1, Nota 2, Nota 3, Nota 4).
> Ao clicar em "Calcular Média", o programa:
> 1. Calcula a média das 4 notas
> 2. Mostra a média
> 3. Mostra `"✅ Aprovado"` se média ≥ 5, ou `"❌ Reprovado"` se abaixo
>
> 💡 Dica: use `float()` para converter os valores dos Entry

✅ Foco: múltiplos Entry, média, condicional simples

---

**Desafio 4.5 — Gerador de Apelido** *(~20 min)*

> Crie um app onde o usuário digita o primeiro nome e escolhe uma "categoria" usando um `CTkOptionMenu` (menu dropdown).
> As opções são: `"Esporte"`, `"Tecnologia"`, `"Anime"`
>
> O botão "Gerar Apelido" cria um apelido combinando nome + categoria:
> - Esporte: `"[nome] Gol de Placa"`
> - Tecnologia: `"[nome].exe"`
> - Anime: `"[nome]-kun"`
>
> **Novo widget — CTkOptionMenu:**
> ```python
> opcoes = ctk.CTkOptionMenu(app, values=["Esporte", "Tecnologia", "Anime"])
> opcoes.pack(pady=10)
> # Para ler: opcoes.get()
> ```

✅ Foco: novo widget (OptionMenu), if/elif, concatenar string

---

### ⭐⭐⭐ Nível 3 — Projetos Completos

---

**Desafio 4.6 — Cronômetro Visual** *(~25 min)*

> Crie um cronômetro simples com:
> - Um Label grande mostrando `"00 segundos"`
> - Um botão "Iniciar" e um botão "Zerar"
>
> Ao clicar em "Iniciar", o número deve aumentar a cada segundo.
>
> **Novo conceito — `after()`:**
> ```python
> # app.after(milissegundos, função) chama uma função depois de um tempo
> # Exemplo: app.after(1000, contar)  → chama contar() após 1 segundo (1000ms)
> ```
>
> 💡 Dica de estrutura:
> ```python
> contando = False
> segundos = 0
>
> def iniciar():
>     global contando
>     contando = True
>     contar()
>
> def contar():
>     global segundos
>     if contando:
>         segundos += 1
>         label_tempo.configure(text=f"{segundos:02d} segundos")
>         app.after(1000, contar)
> ```

✅ Foco: `global`, `after()`, lógica de estado

---

**Desafio 4.7 — App de Recados** *(~30 min)*

> Crie um mini app de recados com:
> - Um Entry para o usuário escrever um recado
> - Um botão "Adicionar"
> - Um `CTkTextbox` que acumula todos os recados digitados, um por linha
> - Um botão "Limpar Tudo" que apaga o Textbox
>
> **Como inserir texto no Textbox:**
> ```python
> caixa.insert("end", "Novo texto\n")  # insere no fim
> caixa.delete("0.0", "end")           # apaga tudo
> ```

✅ Foco: CTkTextbox, acumular dados em tempo de execução

---

## BLOCO 5 — Desafio Final com JSON (30 min)

### Objetivo
O aluno aprende a salvar e carregar dados em um arquivo `.json`, incluindo o caminho de uma imagem — conectando a interface gráfica com persistência real de dados.

---

### Introdução rápida ao JSON (5 min)

> "JSON é um arquivo de texto que guarda informações organizadas. Parece um dicionário do Python."

```json
{
  "nome": "Naruto Uzumaki",
  "anime": "Naruto Shippuden",
  "poder": "⚡ Raio",
  "nivel": 9001,
  "imagem": "C:/usuarios/aluno/desktop/naruto.png"
}
```

> 💡 **Repare:** a imagem não está dentro do JSON — só o **endereço** de onde ela está no computador. Quando carregarmos, o Python vai até esse endereço e abre a imagem.

> ⚠️ **Aviso importante para os alunos:** se você mover ou renomear a imagem depois de salvar, o programa não vai conseguir carregá-la. O JSON guarda o caminho, não o arquivo.

**No Python:**
```python
import json

# Salvar
dados = {"nome": "Naruto", "nivel": 9001, "imagem": "naruto.png"}
with open("ficha.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)

# Carregar
with open("ficha.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
print(dados["nome"])   # Naruto
print(dados["imagem"]) # naruto.png
```

---

### 🎯 Desafio Final — Ficha com Memória

> Expanda o Gerador de Ficha do Bloco 3 para incluir:
>
> **Botão "💾 Salvar Ficha":** salva todos os campos + o caminho da imagem em `ficha.json`
>
> **Botão "📂 Carregar Ficha":** abre `ficha.json`, preenche os campos e recarrega a imagem na tela
>
> Se o arquivo não existir, mostrar aviso. Se o caminho da imagem no JSON não existir mais no computador, mostrar aviso mas carregar o resto normalmente.

---

### Gabarito do Desafio Final

```python
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
        filetypes=[("Imagens", "*.png *.jpg *.jpeg")]
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
        "nome":    nome,
        "anime":   anime,
        "poder":   opcao_poder.get(),
        "nivel":   nivel,
        "imagem":  caminho_imagem   # salva o caminho, não a imagem em si
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

    # Preenche os campos do formulário
    entrada_nome.delete(0, "end")
    entrada_nome.insert(0, dados.get("nome", ""))
    entrada_anime.delete(0, "end")
    entrada_anime.insert(0, dados.get("anime", ""))
    entrada_nivel.delete(0, "end")
    entrada_nivel.insert(0, str(dados.get("nivel", "")))
    opcao_poder.set(dados.get("poder", "🔥 Fogo"))

    # Tenta carregar a imagem do caminho salvo
    caminho_imagem = dados.get("imagem", "")
    if caminho_imagem and not _aplicar_imagem(caminho_imagem):
        label_status.configure(text="📂 Ficha carregada! (imagem não encontrada)", text_color="orange")
    else:
        label_status.configure(text="📂 Ficha carregada com sucesso!", text_color="lightgreen")

    # Atualiza o card com os dados carregados
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

ctk.CTkButton(frame_botoes, text="⚔️ Gerar",      command=gerar_ficha, width=120,
              fg_color="#8b0000", hover_color="#a00000").grid(row=0, column=0, padx=5)
ctk.CTkButton(frame_botoes, text="💾 Salvar",      command=salvar,      width=120,
              fg_color="#2d6a4f").grid(row=0, column=1, padx=5)
ctk.CTkButton(frame_botoes, text="📂 Carregar",    command=carregar,    width=120,
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
```

---

## Referência Rápida — Widgets CustomTkinter

| Widget | Para que serve | Leitura |
|---|---|---|
| `CTkLabel` | Exibir texto | `.configure(text=...)` |
| `CTkButton` | Botão clicável | `command=função` |
| `CTkEntry` | Campo de texto (1 linha) | `.get()` |
| `CTkTextbox` | Área de texto (várias linhas) | `.get("0.0", "end")` |
| `CTkFrame` | Agrupar widgets | — |
| `CTkOptionMenu` | Menu dropdown | `.get()` |
| `CTkImage` | Carrega imagem (requer Pillow) | `CTkLabel(image=...)` |

---

## Referência Rápida — Layout

| Método | Uso ideal |
|---|---|
| `.pack()` | Empilhar widgets, layouts simples |
| `.grid(row=, column=)` | Formulários, layouts em tabela |

---

## Referência Rápida — JSON

```python
import json

# Salvar dicionário em arquivo (inclui caminho de imagem)
dados = {"nome": "Naruto", "nivel": 9001, "imagem": "C:/desktop/naruto.png"}
with open("ficha.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)

# Carregar arquivo para dicionário
with open("ficha.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Usar o caminho de imagem salvo
from PIL import Image
import os
if os.path.exists(dados["imagem"]):
    img = Image.open(dados["imagem"])
```

---

*Plano elaborado para turmas do ensino médio público — progressão pedagógica com vitórias rápidas e desafios graduais.*
