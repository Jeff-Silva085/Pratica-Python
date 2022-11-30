'''
Crie um algoritmo que leia o percurso em quilômetros, o tipo do carro e informe o consumo de combustível, 
sabendo-se que um carro tipo A faz 12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C faz 8 km
'''

perc = float(input('Quantos KM foram percorridos? '))
t_carro = input('Qual tipo de carro foi usado? [A - B - C] ')
t_carro = t_carro.upper()

if t_carro == 'A':
    consumo = perc / 12

elif t_carro == 'B':
    consumo = perc / 9

elif t_carro == 'C':
    consumo = perc / 8

print(f'Seu consumo foi de {consumo} L/Km')

'oO0'

teste 



