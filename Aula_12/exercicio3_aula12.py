def anoBi(n):
    if (n % 4 == 0 and (n % 400 == 0 or n % 100 != 0)):
        return 1
    else:
        return 0
ano = int(input("Insira um ano"))
if (anoBi(ano) == 1):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")