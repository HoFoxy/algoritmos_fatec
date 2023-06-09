idade = int(input("Insira sua idade"))
if idade <= 7:
    print("Vocês está na categoria infantil")
elif idade <= 10:
    print("Vocês está na categoria juvenil")
elif idade <= 15:
    print("Vocês está na categoria adolescente")
elif idade <= 30:
    print("Vocês está na categoria adulto")
else:
    print("Vocês está na categoria sênior")