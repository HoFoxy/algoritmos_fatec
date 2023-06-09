nomes = {}
for i in range(3):
    nome = input("Insira o nome")
    idade = int(input("Insira a idade"))
    nomes[nome] = idade
older = max(nomes.values())
for nome, idade in nomes.items():
    if idade == older:
        print(f"A pessoa com maior idade é: {nome}")