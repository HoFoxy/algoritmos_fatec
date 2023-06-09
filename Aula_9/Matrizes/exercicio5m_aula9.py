matriz = []
maior = 0
pos_x = 0
pos_y = 0
for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input(f"Digite o valor para a posição {i+1},{j+1}: "))
        linha.append(elemento)
        if elemento > maior:
            maior = elemento
            pos_y = j
            pos_x = i
    matriz.append(linha)
print(f"O maior valor é {maior} e está na posição {pos_x}, {pos_y} da matriz")
print("Obs: posição iniciada do 0!")
