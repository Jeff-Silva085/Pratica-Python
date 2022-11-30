# minha resposta
"""
nome = (input("Digite seu nome completo: "))
idade = int(input("Informe sua idade: "))
notaprova1 = float(input("Digite sua Nota da prova 1: "))
notaprova2 = float(input("Digite sua Nota da prova 2: "))

nome = nome.lower().title()
media = (notaprova1 + notaprova2)/2

print(nome)

if media >= 6:
    print(f"Parabéns, sua média é de: {media}")
    print("APROVADA por nota")
else:
    print("Desculpe, mas sua média não é suficiente")
    print(f"Sua média foi: {media}")

if idade >= 18:
    print("Parabens! você tem idade suficiente para ingressar na faculdade!")
    print("idade APROVADA")
else:
    print("Infelizmente você não tem idade suficiente!")

print(f"idade informada: {idade}")

"""

#correção

nome = (input("Digite seu nome completo: "))
idade = int(input("Informe sua idade: "))
notaprova1 = float(input("Digite sua Nota da prova 1: "))
notaprova2 = float(input("Digite sua Nota da prova 2: "))

nome = nome.lower().title()
media = (notaprova1 + notaprova2)/2

if media >= 6 and idade >= 18:
    print("{} foi aprovado!".format(nome))
else:
    print("{} foi reprovado!".format(nome))