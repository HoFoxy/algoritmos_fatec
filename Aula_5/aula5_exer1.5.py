import datetime
from datetime import date
nascimento = int(input("Insira o ano de seu nascimento"))
idade = datetime.date.today().year - nascimento
if idade >= 16:
    print("Parabéns, você pode votar nas eleições")
    if idade >= 18:
        print("Parabéns, já pode tirar CNH também!")