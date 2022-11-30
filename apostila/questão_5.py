'''
Considerando as faixas de valores especificadas abaixo, escreva um algoritmo que, para um determinado 
valor inteiro, mostre qual sua faixa. 
    Faixa A Valores abaixo de 100; 
    Faixa B Valores entre 100 e 150 (inclusive extremos); 
    Faixa C Valores entre 151 e 300 (inclusive extremos); 
    Faixa X Quaisquer outros valores
'''

numero = int(input("digite seu valor: "))

if numero <= 100:
    print('Este valor pertence a faixa A')

elif numero <= 150:
    print('Este valor pertence a faixa B')

elif numero <= 300:
    print('Este valor pertence a faixa C')

else:
    print('Este valor pertence a faixa X')