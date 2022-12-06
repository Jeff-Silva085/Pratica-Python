contador = 0

numero = float(input('digite um número: '))

maior = numero
menor = numero

while contador < 9:
    numero = float(input('digite um número: '))

    if numero >  maior:
        maior = numero

    else:
        if numero < menor:
            menor = numero

    contador += 1

print('este é o numero maior {mai}\nEste é o número menor {men}'.format(mai = maior, men = menor))