medida = float(input('Digite uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
m = medida
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {} m é o mesmo que estes valores: \n{} km \n{} hm \n{} dam \n{:.0f} m \n{:.0f} dm \n{:.0f} cm \n{:.0f} mm '.format(medida, km, hm, dam, m, dm, cm, mm))
