espaco = ' '
primeiro_nome = input("Insira seu primeiro nome").strip()
sobrenome = input("Insira seu sobrenome").strip()
nome = primeiro_nome + ' ' + sobrenome
value_names = []
valores_nome = list(map(ord, nome))

nome_cripto = ""
for indice in range(0, len(nome)):
    nome_cripto = nome_cripto + chr(ord(nome[indice])+1)

print(f"Criptografamos seu nome, você é o: {nome_cripto}")