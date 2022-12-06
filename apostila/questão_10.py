'''
 === QUESTÃO CONFUSA ===
contador = 0
tsa = 0
tsr = 0

while contador < 5:
    contador += 1

    categoria = input('Informe sua categoria na empresa: A / B / C: ').upper()
    
    if (categoria != 'a') and (categoria != 'b'):
        print('CATEGORIA INVALIDA, TENTE NOVAMENTE!')
        contador -= 1

    else:
        salario = float(input('Informe seu salário: '))
        tsa = tsa - salario
'''