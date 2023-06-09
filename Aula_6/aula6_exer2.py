valor = float(input("Insira o valor da compra"))
desconto = 0
if valor <= 1000:
    print("Você recebeu 10% de desconto")
    desconto = 0.1
    print(f"O novo valor é: {valor - (valor*desconto)}")
elif valor >= 1001 and valor <= 5000:
    print("Você recebeu 20% de desconto")
    desconto = 0.2
    print(f"O novo valor é: {valor - (valor*desconto)}")
else:
        print("Você recebeu 30% de desconto")
        desconto = 0.3
        print(f"O novo valor é: {valor - (valor * desconto)}")