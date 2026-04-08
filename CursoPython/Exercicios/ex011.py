larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('A parede tem uma dimensão de {}x{}m², e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('A sua parede cujo a área é de {}m², precisa exatamente de {}l de tinta para pintá-la por completo!'.format(area, tinta))