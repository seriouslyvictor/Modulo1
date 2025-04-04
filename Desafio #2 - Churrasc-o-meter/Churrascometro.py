#  Desafio #2 -- Churrasc-o-meter!  
#  Chegou a hora de mostrar suas habilidades como Mestre do Churrasco™!
#  Você foi convocado para organizar um churrascão de respeito e, claro, precisa garantir que ninguém fique com fome (ou sede!). 
#  Sua missão é construir um planejador de churrasco que, com base em 2 perguntas, calcule tudo o que precisa ser comprado:
#  1 - Quantos adultos vão comparecer?
#  2 - Quantas crianças vão participar?

#  Com esses dados em mãos, o sistema calcula:
#  - A quantidade total de carne (300g por adulto, 150g por criança)
#  - A quantidade de acompanhamentos (200g por pessoa, independente da idade)
#  - Bebidas alcoólicas (2,5L por adulto)
#  - Refrigerantes ou sucos (1L por criança)

#  O resultado final aparece no console, no melhor estilo checklist pré-churrasco.  










print("Bem vindo ao Churrasc-o-meter! Vamos planejar esse Churrasco!.")

adults = int(input("Número de Adultos: "))
kids = int(input("Número de Crianças: "))


meat_per_adult = 300
meat_per_kid = 150    
sides_per_person = 200  
adult_drink = 2.5  
kid_drink = 1.0    

total_meat = (adults * meat_per_adult) + (kids * meat_per_kid)
total_sides = (adults + kids) * sides_per_person
alcoholic_drinks = adults * adult_drink
non_alcoholic_drinks = kids * kid_drink


print("\n--- Churrasc-o-meter calculado ---")
print(f"Total de Carne necessário: {total_meat / 1000:.2f} kg")
print(f"Total de petiscos/entradas: {total_sides / 1000:.2f} kg")
print(f"Quantidade de bebidas: {alcoholic_drinks:.2f} litros")
print(f"Quantidade de refrigerante/sucos: {non_alcoholic_drinks:.2f} litros")
