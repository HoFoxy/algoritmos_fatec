cm_degrau = float(input("Insira a altura dos degraus (em CM)"))
altura_obj = float(input("Insira a altura a se alcançar")) * 100

tot_degraus = altura_obj / cm_degrau
print(f"Você terá que subir {tot_degraus} para alcançar a altura desejada")