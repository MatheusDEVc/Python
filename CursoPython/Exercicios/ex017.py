from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa irá medir {:.2f}'.format(hi))