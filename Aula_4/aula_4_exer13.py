sal = float(input("Insira o salário mínimo"))
qWatts = int(input("Insira a qtd. de Quilowatts gastos"))

preco_qWatts = sal/8
pagar_qWatts = qWatts*preco_qWatts
pagar_desc_qWatts = pagar_qWatts - (pagar_qWatts * 0.15)
print(f"O valor de cada quilowatt é R${preco_qWatts:.2f}")
print(f"Deve ser pago R${pagar_qWatts:.2f}")
print(f"Com desconto, o valor a ser pago é R${pagar_desc_qWatts}")
