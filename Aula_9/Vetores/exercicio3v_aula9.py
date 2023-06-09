valores1 = []
valores2 = []
for i in range(10):
    valor = int(input("Insira valores inteiros"))
    if i < 5:
        valores1.append(valor)
    else:
        valores2.append(valor)
for i in range(min(len(valores1), len(valores2))):
    if i < len(valores1):
        print(valores1[i], end='')
    if i < len(valores2):
        print(valores2[i], end='')
