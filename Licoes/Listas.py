# O que é uma lista em Python?
# Uma lista é uma coleção de itens que podem ser de diferentes tipos, como números, strings, ou até mesmo outras listas. Elas são mutáveis, o que significa que você pode alterar os itens depois de criá-las.
# Também podemos chamar listas de Estrutura de dados.

# Vamos criar uma lista de Deuses gregos.
deuses = ["Zeus", "Afrodite", "Hades"]

# Exibindo toda a lista
print("Nossa lista de Deuses:", deuses)

# Acesando itens da lista
# Podemos acessar itens individuais da lista usando seus índices. Lembre-se de que os índices começam em 0.
print("O primeiro Deus é:", deuses[0])  
print("O segundo Deus é:", deuses[1])
print("O último Deus é:", deuses[-1])

# Acrescentando um item à lista
deuses.append("Poseidon")  # Adiciona "Poseidon" ao final da lista
print("Depois de adicionar Poseidon:", deuses)

# Inserindo um item em uma posição específica
deuses.insert(1, "Ares")
print("Depois de inserir Ares na segunda posição:", deuses)

# Removendo itens da lista
deuses.remove("Ares")
print("Depois de remover Ares:", deuses)

# Alterando um item da lista
deuses[0] = "TIBÚRCIO"
print("Depois de alterar o primerio Deus:", deuses)

# Verificando se um item está na lista
if "Afrodite" in deuses:
    print("Sim, Afrodite está na lista de Deuses!")

# Resgatando o tamanho da lista
print("O número de Deuses na lista é:", len(deuses))

# Categorizando os deuses
deuses.sort()
print("Deuses categorizados:", deuses)

# Revertendo a lista
deuses.reverse()
print("Deuses na ordem invertida:", deuses)

# Lembre-se, listas podem conter diferentes tipos de dados, como números e strings!
nums = [25, 26, 11, 60, 47, 1]
print("Números da megasena:", nums)

# Sorting numbers
nums.sort()
print("Números categorizados:", nums)

