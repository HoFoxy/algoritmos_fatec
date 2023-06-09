from math import sqrt

num = int(input("Insira um número"))
if num < 0:
    print("ERRO")
# a)
num_quadrado = num**2
# b)
num_cubo = num**3
# c)
num_raiz = sqrt(num)
print(f"O número {num} ao quadrado é {num_quadrado}, ao cubo é {num_cubo} e sua raíz é {num_raiz:.0f}")