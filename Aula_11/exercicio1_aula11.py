elementos = []
for i in range(3):
    elemento = int(input("A"))
    elementos.append(elemento)
elementos = tuple(elementos)
print(elementos[::-1])
