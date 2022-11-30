"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

Ganho_hora = float(input('Quando você ganha por hora?: '))
n_horas = int(input('Quantas horas você trabalhou no mês?: '))

salario = n_horas * Ganho_hora

print('Seu salário esse mês foi de {:.2f} reais'.format(salario))