data = input("Insira a data (DD/MM/AAAA)").strip()
dia = data[0:2]
mes = data[3:5]
ano = data[6:]
nova_data = ano + '/' + mes + '/' + dia
print(nova_data)