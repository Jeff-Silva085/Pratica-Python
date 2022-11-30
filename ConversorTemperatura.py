"""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

t_Fahrenheit = float(input('qual a temperatura em fahrenheit?: '))

t_celsius = ((t_Fahrenheit - 32) / 9) * 5

print('A temperatura está em {:.1f}º C'.format(t_celsius))