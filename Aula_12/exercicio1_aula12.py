def testeVF(a):
    if  a % 2 == 0:
        return True
    else:
        return False

n1 = int(input("Insira um número inteiro"))
if not testeVF(n1):
    print("O valor passado não é par")
else:
    print("O valor passado é par")