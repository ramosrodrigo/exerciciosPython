def converte_int(itens):
    novalista=[]
    for x in itens:
        n = float(x)
        novalista.append(n)
    return novalista
    
itens=input().split()

n=converte_int(itens)

codigo=int(n[0])
qtd=int(n[1])
cu=n[2]
custo=cu*qtd

if cu > 0:
    print("Item mais caro")
    print("Codigo: ", codigo)
    print("Quantidade: ", qtd)
    print("Custo: {:.2f}".format(custo))
