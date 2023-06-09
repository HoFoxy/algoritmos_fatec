def tempo(a,b=0,c=0):
    return (a * 3600 + b * 60 + c)
hora = input("Insira hora")
h = hora.split(":")
seg = tempo(int(h[0]), int(h[1]), int(h[2]))
print(f"O total é {seg} segundos")