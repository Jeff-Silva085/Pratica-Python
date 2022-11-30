cont = 0
cont_impares = 0
cont_pares = 0

while cont < 5:
    numero = int(input('Digite um número: '))

    res = numero % 2

    if res == 0:
        cont_pares += 1

    else:
        cont_impares += 1

    cont += 1

print(f'são {cont_impares} impares e {cont_pares} pares!')