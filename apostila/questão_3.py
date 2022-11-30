#3. Leia um número e mostre uma das seguintes mensagens: “É múltiplo de 3” ou 
#“Não é múltiplo de 3”.

n1 = int(input("Digite um número: "))

resto = n1 % 3

if resto == 0:
    print("este valor é multiplo de 3!")
else:
    print("Este valor não é multiplo de 3!")