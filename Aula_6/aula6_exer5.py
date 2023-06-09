pontos = int(input("Insira sua pontuação"))
if pontos <= 49:
    print("Você tirou D")
elif pontos >= 50 and pontos <= 69:
    print("Você tirou C")
elif pontos >= 70 and pontos <= 89:
    print("Você tirou B")
else:
    print("Você tirou A")