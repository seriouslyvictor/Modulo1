#Vamos conhecer os tipos de dados em Python
# Manipulando strings, subscripting
print("Hello"[0])

# Isso ainda é string
print("123" + "456") 

# Integer
print(2025 - 1997)
# Ainda é integer, com separadores de milhar

print(20_000_000)

# AVISO: Jamais usar o . ou , como separadores de milhar
print(20,000,000)



#Boolean - Tipo de dado geralmente usado em CONDICIONAIS para tomar decisões no Software
print(True)
print(False)

# Porquê isso importa:
# Imagine que uma máquina de processar laranjas recebe pedras no lugar de laranjas
# Algumas funções em python se comportam do mesmo jeito, esperam um determinado tipo de dado para que possam funcionar
# len(123456)
print(type(123))
print(type(3.14))
print(type("3.14"))
print(type(True))

# Conversores:
int()
float()
str()
bool()

# Operadores matemáticos em Python
print(123 + 456)
print(2025 - 1997)
print(3 * 10)
print(100 / 5)
print(100 // 5)
print(2**2)

# LEMBRE-SE: A ordem das operações está presente também em programação () ** * ou / + ou -
print(3 * 3 + 3 / 3 - 3)

#Desafio - Churrascometro