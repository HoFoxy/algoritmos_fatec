from random import randint
numeros = [0] * 13
for _ in range(30000):
    jogada1 = randint(0, 6)
    jogada2 = randint(0, 6)
    tot = jogada2 + jogada1

    numeros[tot] += 1

tot_jogadas = sum(numeros[2:])
jogadas_7 = numeros[7] / tot_jogadas
print("Frequência das somas:")
for tot in range(2, 13):
    print(f"Soma {tot}: {numeros[tot]}")

print(f"\nFrequência da soma 7: {jogadas_7:.2f}")