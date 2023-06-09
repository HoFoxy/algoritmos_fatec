base = float(input("Insira a base"))
while base <= 0:
    print("Insira valores válidos!")
    base = float(input("Insira a base"))

altura = float(input("Insira a altura"))
while altura <= 0:
    print("Insira valores válidos!")
    altura = float(input("Insira a altura"))

area = base*altura/2
print(f"A área do triângulo é {area}")

