soma = 0
numeros = int(input("Quantos números você quer somar os pares?"))
for i in range(1, numeros+1):
    if i % 2 == 0:
        soma = soma + i
        print(soma, i)
    else:
        continue
    if i == 50:
        break
if numeros > 50:
    print(f"Haha, somei só os 50 primeiros números e deu... {soma}")
else:
    print(f"Somei os {numeros} primeiros números e deu... {soma}")