sal = float(input("Insira seu salário"))
sal_raise = float(input("Insira a % de aumento"))
novo_sal = sal* (sal_raise / 100 + 1)
print(f"Seu novo salário é R${novo_sal:.2f}")