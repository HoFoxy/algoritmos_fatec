def animais(patas):
    patos = 0
    coelhos = 0
    for i in range(cabecas+1):
        j = cabecas - i
        if (i * 2) + (j * 4) == patas:
            patos = i
            coelhos = j
            break
    return patos, coelhos
cabecas = int(input("Insira a qtd de cabeças"))
if cabecas % 2 == 0:
    cabecas -= 1
    print("Aparentemente, um animal é paraplégico... Vamos desconsiderar ele.")
patas = cabecas*3+1

patos, coelhos = animais(patas)
print(f'Há {patas} patas no cercado')
print(f"A quantidade de patos é {patos} e de coelhos é {coelhos}")