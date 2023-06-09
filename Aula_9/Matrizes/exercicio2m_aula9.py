matriz = []
maior = 0
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
        if elemento > maior:
            maior = elemento
    matriz.append(linha)
for i in matriz:
    for j in i:
        print(j * maior)
