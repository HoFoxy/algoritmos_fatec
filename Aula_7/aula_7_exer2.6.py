#Fatorial
import math
from math import factorial

fatorial = int(input("Insira o número a se fatorar"))
while fatorial < 0:
    print("Não há fatorial negativo")
    fatorial = int(input("Insira o número a se fatorar"))

resultado_fatorial = math.factorial(fatorial)
print(f"O fatorial de {fatorial}! é: {resultado_fatorial}")