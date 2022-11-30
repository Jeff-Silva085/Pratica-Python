#2. Uma loja de eletrodomésticos oferece um desconto de 10% para compras superiores a R$ 1.000,00. Crie um 
#algoritmo que receba o valor da compra e mostre o valor a pagar.

valor_compra = float(input("Informe o valor da compra: "))
desconto = 0

if valor_compra > 1000:
    desconto = valor_compra *  0.1

valor_pagar = valor_compra - desconto

print("Valor a pagar é de: {}".format(valor_pagar))