soma = 0
contador = 0
for i in range(1000):
    num = int(input("Insira um número inteiro e par:"))
    if num % 2 == 0:
        soma += num
    if num == 0:
        break
    contador += 1
media = soma / contador
print(f"A média da soma dos valores pares é {media}")