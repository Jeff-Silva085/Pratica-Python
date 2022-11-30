'''
Numa determinada empresa, os salários dos funcionários do setor de Recursos Humanos (RH) terão um 
aumento de acordo com a tabela abaixo:

Faixa salarial Percentual de Reajuste 
Salário < R$ 1.000,00 10% 
R$ 1.000,00 < = Salário < R$ 2.000,00 8% 
Salário > = R$ 2.000,00 6% 

Escreva um programa que leia o salário do funcionário e o seu setor e, caso ele tenha direito ao aumento, 
calcule e mostre o seu salário reajustado. 
'''

setor = input('Informe qual seu setor: ')
setor = setor.upper()

if setor == 'RH':

    salario = float(input('Informe seu salário: '))
    if salario < 1000:
        salr = salario + salario * 0.1

    elif salario <= 2000:
        salr = salario + salario * 0.08

    elif salario > 2000:
        salr = salario + salario * 0.06

    print(f'Seu novo salário é de: {salr}')
else:
    print('Seu setor não houve aumento!')