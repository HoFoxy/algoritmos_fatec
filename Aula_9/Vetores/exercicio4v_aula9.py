frases = []
while len(frases) < 20:
    palavra = input("Insira uma palavra de 10 caracteres").strip()
    frases.append(palavra)
frase = ','.join(frases)
print(frase[::-1])