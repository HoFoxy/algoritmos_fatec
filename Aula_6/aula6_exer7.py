largura = float(input("Digite a largura do aposento em metros: "))
comprimento = float(input("Digite o comprimento do aposento em metros: "))
altura = 2.8
tinta_lata = float(input("Digite a quantidade de tinta por lata em litros: "))

area_paredes = 2 * (largura + comprimento) * altura - largura * altura - (0.8 *2.1)
qtd_latas = area_paredes / (tinta_lata * 3)

print(f"Serão necessárias {round(qtd_latas)} latas de tinta para pintar o aposento")