from random import randint
#jogadas = []
#dado = 0
#for i in range(6000):
#    dado = randint(1, 6)
#    jogadas.append(dado)
#dados_1 = (jogadas.count(1) / 6000) * 100
#dados_2 = (jogadas.count(2) / 6000) * 100
#dados_3 = (jogadas.count(3) / 6000) * 100
#dados_4 = (jogadas.count(4) / 6000) * 100
#dados_5 = (jogadas.count(5) / 6000) * 100
#dados_6 = (jogadas.count(6) / 6000) * 100

#Ou sem usar tanto espaço...
jogada = [0]*7
estatistica = [0]*7
for i in range(6000):
    x = randint(1, 6)
    jogada[x] = jogada[x] + 1
for i in range(1, 7):
    estatistica[i] = (jogada[i] / 6000)
for i in range(1, 7):
    print(f"Lado {i} foi sorteado {jogada[i]} vezes/ = {estatistica[i]:.2%}")
#print(f"A frequência é, respectivamente (1,2,3,4,5,6): {dados_1:.2f}%, {dados_2:.2f}%, {dados_3:.2f}%, {dados_4:.2f}%, {dados_5:.2f}%, {dados_6:.2f}%", end='')