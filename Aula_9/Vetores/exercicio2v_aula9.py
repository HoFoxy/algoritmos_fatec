valores = []
maior = 0
pos = 0
for i in range(5):
    x = int(input("Insira um valor inteiro"))
    if x > maior:
        maior = x
        pos = i
    valores.append(x)
print(f"O maior valor do vetor é: {maior} e sua posição é {pos}")