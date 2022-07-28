#funcao para somar elementos de uma lista
#(len conta os elementos de uma lista)
def somar(s):
    soma=0
    tamanho=len(s)
    i=0
    while i<tamanho:
        soma=soma+s[i]
        i=i+1
    return soma

lista=[1,3,6,9,10]
a=somar(lista)
print(a)

#mesma funcao mas com FOR

def soma(s,n):
    so=0
    tam=len(s)
    for i in range(0,tam,1):
        so=so+s[i]
    return so
        


#funcao contar para contar quantas vezes um elemento numa lista se repete
def contar(s,n):
    contando=0
    tamanho=len(s)
    incremento=0
    while incremento < tamanho:
        if s[incremento]==n:
            contando=contando+1
        incremento=incremento+1
    return contando

li=[1,9,4,1,8,1,1,4]
a=contar(li,1)
print(a)
