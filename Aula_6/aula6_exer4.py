tipo_combustivel = input("Insira se é álcool, diesel ou gasolina (A, D ou G)").upper()
qtd_combustivel = int(input("Quantos litros você abasteceu?"))
alcool = 1.7997
diesel = 0.9798
gasolina = 2.1009
if tipo_combustivel == "A":
    print(f"O valor a se pagar é: R${qtd_combustivel*alcool:.2f}")
elif tipo_combustivel == "D":
    print(f"O valor a se pagar é: R${qtd_combustivel * diesel:.2f}")
elif tipo_combustivel == 'G':
    print(f"O valor a se pagar é: R${qtd_combustivel * gasolina:.2f}")
else:
    print("Input inválido")