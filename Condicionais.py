# Condicionais são usadas para tomar decisões com base nos valores booleanos verdadeiro ou falso.
# As condicionais podem ser simples ou compostas, com ajuda de operadores lógicos para determinar o resultado.

# What is an if statement?
# It lets the program make a decision based on a condition.

# Basic structure:
# if condition:
#     do something

# Here's a basic example:
age = 18

if age >= 18:
    print("You are an adult!")

# If the condition is false, nothing happens.
# Let's add an 'else' to handle the other case.

age = 16

if age >= 18:
    print("You are an adult!")
else:
    print("You are not an adult yet.")

# We can also add 'elif' (which means "else if") to check more than one condition.

temperature = 25

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("The weather is nice.")
else:
    print("It's a bit cold today.")

# Comparison operators we can use in if statements:
# ==  means equal
# !=  means not equal
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to

# Logical operators (for combining conditions):
# and  --> both must be true
# or   --> at least one must be true
# not  --> reverses the condition

# Example using 'and':
money = 10
hungry = True

if money >= 5 and hungry:
    print("You can buy a snack!")

# Example using 'or':
is_raining = False
have_umbrella = True

if is_raining or have_umbrella:
    print("You're good to go outside!")

# Example using 'not':
logged_in = False

if not logged_in:
    print("Please log in to continue.")

# You can also use variables that are already True/False (called booleans)

is_hungry = True

if is_hungry:
    print("Time to eat!")
else:
    print("Not hungry right now.")

#Desafio Power Lifters
#Desafio Pizza-o-tron