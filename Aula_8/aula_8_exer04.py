frase = input("Insira uma frase").strip()
qtd = 0
for letra in frase:
    if (frase in 'aeiouáéíóúàèìòùâêîôûäëïöüãõ'):
        qtd += 1
print(f"Há {qtd} vogais")