matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = float(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

for i in matriz:
    for j in i:
        print(j)
