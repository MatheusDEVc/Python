dias = int(input('Quantos dias alugado?  '))
km = float(input('Quantos KM percorridos?  '))
calc = (dias * 60) + (km * 0.15)
print('Visando que o carro foi alugado por {} dia(s) e rodou por {}km, o valor a ser pago é de R${:.2f} '.format(dias, km, calc))