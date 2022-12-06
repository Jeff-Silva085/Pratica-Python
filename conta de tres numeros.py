"""
EXERCÍCIO 11

Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo.
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
"""
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = float(input('Digite outro número, inteiro,ou decimal: '))

produto = (numero1*2) + (numero2/2)
print('O resultado do produto é: {}'.format(produto))

somaT = (numero1*3) + numero3
print('O resultado da soma é: {}'.format(somaT))

potencia = numero3**3
print('O resultado da potencia é: {:.1f}'.format(potencia))