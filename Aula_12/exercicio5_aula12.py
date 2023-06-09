def calcEsfera(R):
    volume = 4/3 * (R**3)
    return volume
raio = float(input("Insira o raio da esfera"))
volume = calcEsfera((raio))
print(f"O volume da esfera é {volume:.2f}m3")