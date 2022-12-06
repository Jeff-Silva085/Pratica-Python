"""
13 - Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7

"""
altura = float(input('Informe sua altura em metros: '))

peso_homem = (72*altura) - 58
peso_mulher =(62.1*altura) - 44.7

print('O peso ideal para homens é de {ph:.3f}\nE para mulheres é de {pm:.3f} kg'.format( ph = peso_homem, pm = peso_mulher))