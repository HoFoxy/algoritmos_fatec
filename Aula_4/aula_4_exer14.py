horas_minutos = float(input("Insira as horas (HH,mm)"))
horas = int(horas_minutos)
minutos_dec = (horas_minutos - horas) * 100
if minutos_dec > 60:
    horas +=1
    minutos_dec -= 60
tot_min = horas * 60 + minutos_dec
print(f'Você digitou {horas_minutos}')
print(f'Em minutos, a hora digitada corresponde a {tot_min:.0f}')