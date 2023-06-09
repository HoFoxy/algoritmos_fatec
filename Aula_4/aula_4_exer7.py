deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros (em %): "))

rendimento = deposito * (taxa_juros / 100)
valor_total = deposito + rendimento

print(f"Valor do rendimento: R$ {rendimento:.2f}")
print(f"Valor total após o rendimento: R$ {valor_total:.2f}")