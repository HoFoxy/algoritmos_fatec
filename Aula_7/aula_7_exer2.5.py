pessoas = 0
maior_imc = 0
menor_imc = 0
soma_peso = 0
soma_altura = 0

while pessoas < 20:
    peso = float(input(f"Insira o peso da {pessoas+1}° pessoa:"))
    altura = float(input(f"Insira a altura da {pessoas+1}° pessoa:"))
    imc = peso/altura**2
    if imc > maior_imc:
        maior_imc = imc
    if menor_imc == 0 or imc < menor_imc:
        menor_imc = imc
    soma_peso += peso
    soma_altura += altura
    pessoas += 1

media_peso = soma_peso/pessoas
media_altura = soma_altura/pessoas
print(f"A média dos pesos é {media_peso:.2f}")
print(f"A média das alturas é {media_altura:.2f}")
print(f"O menor IMC é {menor_imc:.1f} e o maior é {maior_imc:.1f}")