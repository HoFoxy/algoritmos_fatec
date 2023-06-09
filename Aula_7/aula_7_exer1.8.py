num = int(input("Digite um número inteiro maior que 1: "))

if num <= 1:
    print("Valor inválido")
    quit()
divisor = 2
primo = True

for divisor in range(2, num):
    if num % divisor == 0:
        primo = False
        break
    divisor += 1

if primo:
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")