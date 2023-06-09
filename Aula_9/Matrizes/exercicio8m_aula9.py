matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        elemento = float(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)
soma = 0
contador = 0

for i in range(0, 5, 2):
    for j in range(5):
        soma += matriz[i][j]
        contador += 1
media = soma/contador
print(f"A média dos elementos é {media:.2f}")