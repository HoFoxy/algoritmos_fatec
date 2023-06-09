#Versao 2.0 do exer01

n = int(input("Insira um nº inteiro"))
b = int(input("Valor base"))
i = 1
e = 0
while i <= n:
    e = e + pow(b, i)
    i += 1
print(f"{e}")