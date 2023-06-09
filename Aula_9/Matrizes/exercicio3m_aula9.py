matriz = []
soma_diag = 0

for i in range(4):
    linha = []
    for j in range(4):
        elemento = float(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)
for i in range(4):
    soma_diag += matriz[i][i]

print(f"Os elementos da matriz são: {matriz}")

print(f"E a soma da matriz é {soma_diag}")