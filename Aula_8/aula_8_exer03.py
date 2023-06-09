numero = input("Insira um número de 9 caracteres")
primeiro = numero[0]
segundo =  numero[1:4]
terceiro = numero[4:7]
decimal = numero[7:]
print(f"O valor formatado é: {primeiro}.{segundo}.{terceiro},{decimal}")