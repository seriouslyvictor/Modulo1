from google import genai
from google.genai import types
import time

#pratica não recomendada, apenas para demonstração e clareza.
GEMINI_API_KEY = "AIzaSyB-zzzzzzzzzzzz" # essa chave é inválida!
MODEL_FAST = "gemini-2.5-flash-lite"

cliente = genai.Client(api_key=GEMINI_API_KEY)


# #solicitando uma resposta para o modelo
# resposta = cliente.models.generate_content(model="gemini-2.5-flash-lite", contents="Faça um Haiku sobre um gato lendário chamado Tibúrcio!")

# #resgatando a resposta do modelo, bem como o uso de tokens
# print(resposta.text)
# if resposta.usage_metadata:
#     print(resposta.usage_metadata.thoughts_token_count)
#     print(resposta.usage_metadata.total_token_count)

# #solicitando uma resposta com parâmetros 
# resposta = cliente.models.generate_content_stream(model="gemini-2.5-flash-lite", contents="Conte me coisas sobre gatos!", config=types.GenerateContentConfig(
#     system_instruction="Suas respostas devem ser curtas e sempre incluir emojis",
# ))

#resgatando a resposta do modelo, bem como o uso de tokens

# #mini-desafio #1 Simples Chat Prompt

# print("Bem vindo ao FoodGrader! Pergunte qualquer coisa relacionada à comida!")
# pergunta = input("Eu quero saber...\n")
# resposta2 = cliente.models.generate_content(model=MODEL_FAST, config=types.GenerateContentConfig(
#     system_instruction="You are an expert nutritionist and must answer all queries related to food with short but precise answers, like a human would in a tweet"
# ) , contents=pergunta)
# print(resposta2.text)
# if resposta2.usage_metadata:
#     print(f"Gastamos {resposta2.usage_metadata.total_token_count} tokens nessa resposta!")

# ========= Respostas estruturadas ===========
# from pydantic import BaseModel
# import enum

# class Habitability(enum.Enum):
#     HABITABLE =  "Habitável"
#     TERRAFORM = "Habitável com tecnologia de terraformação"
#     HOSTILE =  "Inabitável para humanos"


# class Planeta(BaseModel):
#     nome_planeta: str
#     desc: str
#     composicao: str
#     raio: int
#     rotacao: float
#     translacao: float
#     satelites: list[str]
#     habitabilidade: Habitability

# resposta3 = cliente.models.generate_content(model=MODEL_FAST, contents="Forneça todas as informações solicitadas do planeta Júpiter em um formato json",config={"response_mime_type": "application/json" ,"response_schema": Planeta})

# terra_dict = resposta3.text
# print(terra_dict)
# print(resposta3.usage_metadata.total_token_count)

#mini desafio #2 - TODO

# ========== Trabalhando com imagens ============
# A biblioteca Pillow facilita leitura e processamento de imagens, embora não seja obrigatória.
from PIL import Image
#Essas bibliotecas são usadas para baixar os bytes e decodificar os bytes em forma de uma imagem para processamento, essa etapa  é feita implicamente nos navegadores, mas nos bastidores precisamos baixar os bytes
import io, requests

# #abertura de arquivo local
# imagem = Image.open("genAI/blue_marble.jpg")
# image_bytes = requests.get("https://upload.wikimedia.org/wikipedia/pt/b/bf/SpongeBob_SquarePants_personagem.png").content
# image_stream = io.BytesIO(image_bytes)
# img =  Image.open(image_stream)
# # img.show()

# resposta = cliente.models.generate_content(model=MODEL_FAST, contents=[imagem, "Forneça uma legenda para essa imagem."])
# resposta2 = cliente.models.generate_content(model=MODEL_FAST, contents=[img, "Forneça uma legenda para essa imagem."])
# print(resposta.text)
# print(resposta2.text)

# ============== Imagem com saída estruturada ==============
from pydantic import BaseModel
import json
imagem = Image.open("genAI/blue_marble.jpg")


class Planeta(BaseModel):
    nome_planeta: str
    desc: str
    composicao: str
    raio: int
    rotacao: float
    translacao: float
    satelites: list[str]

prompt = """
Você é um especialista em planetas e irá analisar imagems para descobrir e fornecer informações sobre o mesmo.
Se não for possível indentificar o planeta, tente imaginar quais seriam suas características com base na imagem e correlacionando com outros planetas que você já conhece. 
"""

resposta = cliente.models.generate_content(model=MODEL_FAST, contents=[imagem,prompt], config=types.GenerateContentConfig(
    response_mime_type= "application/json",
    response_schema= Planeta,
))

planeta_dict = None
if resposta.text != None:
    print(resposta.text)
    planeta_dict = json.loads(resposta.text)



import datetime as dt
agora = dt.datetime.now()
agora_string =  agora.strftime("%d%m%y-%H%M%S")
if planeta_dict and "nome_planeta" in planeta_dict:
    planeta_string = planeta_dict["nome_planeta"].replace(" ", "-")
    try:
        with open(file=f"genAI/{planeta_string}.json", mode="w", encoding="UTF-8") as f:
            json.dump(planeta_dict, f, ensure_ascii=False, indent=4)
    except OSError:
        print("Não foi possível salvar o JSON")


if resposta.usage_metadata:
    print(resposta.usage_metadata.total_token_count)
