nota1 = float(input("Insira a 1° nota"))
nota2 = float(input("Insira a 2° nota"))
nota3 = float(input("Insira a 3° nota"))
media = (nota1 + nota2 + nota3) / 3
print(f"A média aritmética é {media:.2f}")
if media < 3:
    print("Você foi reprovado")
elif media < 7:
        print("Exame")
        nota_exame = float(input("Insira a nota do exame"))
        media = (media + nota_exame) /2
        if media >= 7:
            print(f"A nova média é: {media:.2f}")
            print("Aprovado")
        else:
            print(f"A nova média é: {media:.2f}")
            print("Reprovado")
else:
    print("Aprovado")