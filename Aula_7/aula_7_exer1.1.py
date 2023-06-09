n = int(input("Insira um nº inteiro"))
e = 0
for i in range(n):
    e = e + pow(2,i+1)
print(f"{e}")