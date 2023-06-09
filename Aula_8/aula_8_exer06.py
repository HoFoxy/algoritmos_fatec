palavra = input("Insira uma palavra").lower()
if palavra == palavra[::-1]:
    print("A palavra é palíndroma")
else:
    print("A palavra não é palíndroma")