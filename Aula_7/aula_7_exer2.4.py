continua = 1
soma = 0
contador = 0
while continua == 1:
    idade = int(input("Insira a idade (Digite 0 para parar"))
    if idade == 0:
        continua = 0
    soma += idade
    contador += 1
media  = soma/contador
print(f"A média das idades do grupo é {media:.2f} e quantidade de pessoas é {contador}")