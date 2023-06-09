num1 = int(input("Insira o 1° número"))
num2 = int(input("Insira o 2° número"))
decisao = int(input("O que você quer exibir 1, 2, 3 ou 4? (Media, Diferença, Produto ou Divsão ?)"))
if decisao == 1:
    media = (num1 + num2) / 2
    print(f"A média é {media}")
elif decisao == 2:
    diferenca = max(num1, num2) - min(num1, num2)
    print(f"A diferença entre o maior e o menor número é {diferenca}")
elif decisao == 3:
    produto = num1 * num2
    print(f"O produto dos números é {produto}")
elif decisao == 4:
    divisao = num1 / num2
    print(f"A divisão do 1° número pelo segundo é {divisao}")
else:
    print("Você escolheu um valor inválido")