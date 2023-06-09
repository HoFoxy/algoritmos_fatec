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


def primoSequencial(x):
    i = 2
    lista_primos = []
    while i <= x:
        if primo(i):
            lista_primos.append(i)
        i += 1
    return lista_primos


v = int(input("Insira um número inteiro"))
x = v*2+5
lista_nprimos = primoSequencial(x)
soma = 0
if primo(v):
    print("O número é primo")
else:
    print("O número não é primo")
print(f"Os números primos de 0 a  {x} são: {lista_nprimos}")
for i in range(len(lista_nprimos)):
    soma += lista_nprimos[i]
    i+= 1
print(f"A soma total dos números primos é: {soma}")