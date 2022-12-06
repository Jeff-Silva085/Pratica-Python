"""
15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

ganho_por_hora = float(input('quanto você ganha por hora?: '))
numeros_horas = float(input('quantas horas você trabalha por mês?: '))

salario_mes = numeros_horas * ganho_por_hora

print('Seu salário é de: R${:.2f}'.format(salario_mes))
print('')

#imposto de renda
ir = ((11/100) * salario_mes)
salario_ir = salario_mes - ir

#inss
inss = ((8/100) * salario_ir)
salario_inss = salario_ir - inss

#sindicato
sindicato = ((5/100) * salario_inss)
salario_bruto = salario_inss - sindicato
print(
    'Foi retirado\n\nR${ir:.2f} para imposto de renda\n\nR${inss:.2f} do inss\n\nR${sind:.2f} do sindicato!\n\nRestando apenas R${sal_bruto:.2f} do seu salário!'.format(ir = ir, inss = inss, sind = sindicato, sal_bruto = salario_bruto)
)

