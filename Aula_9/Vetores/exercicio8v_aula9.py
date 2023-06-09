A = []
for _ in range(10):
    valor = int(input(f"Insira o {_+1}º valor"))
    A.append(valor)
B = sorted(A)
print(f"O vetor A possui os valores: {A}")
print(f"O vetor B possui os valores ordenados: {B}")