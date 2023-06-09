num = int(input("Digite um número inteiro maior que 1: "))

while num <= 1:
    num = int(input("Digite um número inteiro maior que 1: "))
divisor = 2
primo = True

while divisor < num:
    if num % divisor == 0:
        primo = False
        break
    divisor += 1

if primo:
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")