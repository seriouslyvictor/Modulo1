#  DESAFIO #4 - COMPETIÇÃO POWER LIFTERS 2024.  
#  Está acontecendo uma competição de POWER LIFTERS e atualmente há 2 atletas competindo, Chris Bumstead e Ramón Dino 
#  Sua missão é criar um código que irá determinar qual dos atletas é o vencedor. 
#  Regras: 
#  1 - Os atletas se desafiam em 4 modalidades, cada modalidade concede uma pontuação de 0 até 200; 
#  2 - Após o término das 4 modalidades, calculamos a média de pontos dos dois atletas. 
#  3 - Por fim, vence o atleta que atingir a maior média, um empate é possível. 
#  COMO CALCULAR MÉDIA? 
#  Some todos os pontos do atleta, divida a soma pelo número de pontos(4); 
#  LEMBRE-SE DA ORDEM DAS OPERAÇÕES NA MATEMÁTICA.   Dados para testar o código: 
#  Chris Bumstead: 127, 185 , 134, 199. 
#  Ramón Dino: 115, 190, 136, 197.


print("🏋️ DESAFIO #4 - COMPETIÇÃO POWER LIFTERS 2024 🏋️")
print("Chris Bumstead vs Ramón Dino — Quem será o campeão?\n")


chris1 = 127
chris2 = 185
chris3 = 134
chris4 = 199


ramon1 = 115
ramon2 = 190
ramon3 = 136
ramon4 = 197


media_chris = (chris1 + chris2 + chris3 + chris4) / 4
media_ramon = (ramon1 + ramon2 + ramon3 + ramon4) / 4


print(f"Média de Chris Bumstead: {media_chris:.2f}")
print(f"Média de Ramón Dino: {media_ramon:.2f}\n")

if media_chris > media_ramon:
    print("🏆 O campeão é CHRIS BUMSTEAD!")
elif media_ramon > media_chris:
    print("🏆 O campeão é RAMÓN DINO!")
else:
    print("🤝 Temos um EMPATE! Ambos os atletas deram o seu máximo!")
