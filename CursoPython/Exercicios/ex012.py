preço = float(input('Digite o valor do produt: R$'))
desconto = preço - (preço * 15 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 15% vai custar R${:.2f}'.format(preço, desconto))