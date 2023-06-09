def primo(n):
    i = 1
    contador = 0
    while i <= n:
        if (n % i) == 0:
            contador += 1
        i += 1
    if contador == 2:
        return True
    else:
        return False

v = int(input("Verificar numeros primos: "))
if primo(v):
    print("O número é primo")
else:
    print("O número não é primo")
i = 2
coluna = 1
while i <= 50:
    if(primo(i)):
        print(i, end=' - ')
        coluna += 1
    i += 1
    if (coluna > 15):
        print()
        coluna = 1