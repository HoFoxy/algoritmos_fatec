a = float(input("Insira o 1° lado do triângulo"))
b = float(input("Insira o 2° lado do triângulo"))
c = float(input("Insira o 3° lado do triângulo"))

if a + b > c and a + c > b and b + c > a:
    print("É um triângulo válido")
else:
    print("Triângulo inválido")
if (a==b) and (b==c):
    print("É um triângulo equilátero")
elif (a==b) and (b==c) and (a==c):
    print("É um triângulo isóceles")
else:
    print("É um triângulo escaleno")