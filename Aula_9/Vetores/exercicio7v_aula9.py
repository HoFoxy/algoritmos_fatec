numeros_primos = []
numero = 101

while len(numeros_primos) < 10:
    is_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            is_primo = False
            break
    if is_primo:
        numeros_primos.append(numero)
    numero += 1

print("Os 10 primeiros números primos acima de 100 são:")
for primo in numeros_primos:
    print(primo)