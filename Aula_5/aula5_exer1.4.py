sexo = input("Insira seu sexo (M ou F)").upper()
altura = float(input("Insira sua altura (metro)"))
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso_ideal:.1f}")
else:
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {peso_ideal:.1f}")