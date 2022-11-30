'''
Crie um algoritmo que leia 8 números e informe quantos destes números estão entre 100 e 200
'''
cont = 0
cont2 = 0

while cont < 8:
    cont += 1

    numero = int(input('digite um número: '))

    if numero > 100 and numero < 200:
        cont2 += 1


print(cont2)