#Leia o sexo, a altura e o peso de uma pessoa e informe, 
# com base na tabela abaixo, se a pessoa está ou não com peso acima do ideal

sexo = str(input("informe seu sexo [M / F]: "))
sexo = sexo.upper()
altura = float(input("infome agora sua altura: "))
peso = float(input("informe também sua peso: "))

if sexo == "M":
    pi = 72.7 * altura - 58
else:
    pi = 62.1 * altura - 44

if peso > pi:
    print("Você está acima do peso!")
else:
    print("Você está no seu peso ideal!")