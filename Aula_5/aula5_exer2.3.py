preco = float(input("Insira o preço do produto"))
origem = int(input("Insira o código de origem 1, 2, 3, 4 ou 5(Sul, Norte, Nordeste, Centro-Oeste ou Sudeste)"))
imposto = 0
if origem == 1:
    imposto = 0.11
elif origem == 2:
    imposto = 0.13
elif origem == 3:
    imposto = 0.09
elif origem == 4:
    imposto = 0.12
elif origem == 5:
    imposto = 0.18
else:
    print("Código inválido")
preco_final = preco - (preco * imposto)
print(f"O preço final para o produto é: R${preco_final:.2f}")