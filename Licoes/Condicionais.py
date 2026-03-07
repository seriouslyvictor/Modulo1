# Condicionais são usadas para tomar decisões com base nos valores booleanos verdadeiro ou falso.
# As condicionais podem ser simples ou compostas, com ajuda de operadores lógicos para determinar o resultado.

# O que é uma declaração if?
# Permite que o programa tome uma decisão baseada em uma condição.

# Estrutura básica:
# if condição:
#     faça algo

# Aqui está um exemplo básico:
idade = 18

if idade >= 18:
    print("Você é maior de idade!")

# Se a condição for falsa, nada acontece.
# Vamos adicionar um 'else' para lidar com o outro caso.

idade = 16

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você ainda não é maior de idade.")

# Também podemos adicionar 'elif' (que significa "senão se") para verificar mais de uma condição.

temperatura = 25

if temperatura > 30:
    print("Está quente lá fora!")
elif temperatura > 20:
    print("O clima está agradável.")
else:
    print("Está um pouco frio hoje.")

# Operadores de comparação que podemos usar em declarações if:
# ==  significa igual
# !=  significa diferente
# >   maior que
# <   menor que
# >=  maior ou igual a
# <=  menor ou igual a

# Operadores lógicos (para combinar condições):
# and  --> ambos devem ser verdadeiros
# or   --> pelo menos um deve ser verdadeiro
# not  --> inverte a condição

# Exemplo usando 'and':
dinheiro = 10
com_fome = True

if dinheiro >= 5 and com_fome:
    print("Você pode comprar um lanche!")

# Exemplo usando 'or':
esta_chovendo = False
tem_guarda_chuva = True

if esta_chovendo or tem_guarda_chuva:
    print("Você está pronto para sair!")

# Exemplo usando 'not':
logado = False

if not logado:
    print("Por favor, faça login para continuar.")

# Você também pode usar variáveis que já são True/False (chamadas booleanos)

esta_com_fome = True

if esta_com_fome:
    print("Hora de comer!")
else:
    print("Não estou com fome agora.")

#Desafio Power Lifters
#Desafio Pizza-o-tron