n = float(input())
soma = 0
cont = 1
while cont <= n:
    if cont %2 == 1:
        termo = 1 / cont
        soma = soma - termo
    else:
        termo = 1 / cont
        soma = soma + termo
    cont = cont + 1
print("{:.6f}".format(soma))
    
    
###########################AC3#######AC3###########AC3###########################

n = float(input())
soma = 0
cont = 1
while cont <= n:
    regra = 1 / (cont**2)
    soma = soma + regra
    cont = cont + 1
    
print("{:.6f}".format(soma))
