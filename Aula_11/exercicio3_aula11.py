lista1 = []
lista2 = []

for i in range(10):
    valor = int(input("Insira um número"))
    if i < 5:
        lista1.append(valor)
    if i >= 5:
        lista2.append(valor)
lista3 = set(lista1).union(lista2)
print(lista3)