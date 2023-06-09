import num
valores = input("Insira seu RA")
valores_sep = [int(i) for i in valores]
soma = 0
multiplica = numpy.prod(valores_sep)
for i in range(len(valores_sep)):
    soma += valores_sep[i]
print(f"A soma dos elementos do RA é {soma}"
      f" e a multiplicação {multiplica}")