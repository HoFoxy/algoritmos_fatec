def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

x = int(input("Insira um número"))
y = int(input("Insira outro número"))
mdc = mdc(x,y)
print(mdc)