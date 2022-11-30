lado = float(input('Informe o lado de um quadrado em cm: '))

area = (lado**2)
dobro_area = area*2

print('A área deste quadrado é de {a:.2f} cm²\nO dobro dela é de {d:.2f} cm²!'.format(a=area, d = dobro_area))