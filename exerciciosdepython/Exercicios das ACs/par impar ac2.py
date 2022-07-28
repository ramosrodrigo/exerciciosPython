numero = int(input())
resto = numero % 2
if resto == 0:
   print("O numero",numero ,"eh par!")
else:
   print("O numero",numero ,"eh impar!")

print('----- Exemplo 2 - seleção composta')

n = int(input('Digite um número inteiro: '))
resto = n % 2
if resto == 0:
    print(n, 'é par')
else:
    print(n, 'é ímpar')

print('----- Fim do Exemplo 2')
print()

largura = float(input())
comprimento = float(input())
altura = float(input())

if largura <= 45:
   print("PERMITIDA")
elif comprimento <= 56:
   print("PERMITIDA")
elif altura <= 25:
   print("PERMITIDA")
else:
   print("PROIBIDA")
