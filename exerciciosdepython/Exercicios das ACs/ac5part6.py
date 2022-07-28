msg = """-----------------------------------
Pizzaria 0.1 - menu de comandos
-----------------------------------
- ajuda: exibe o menu de ajuda
- sair: encerra o programa
- exibir: exibe a lista de pedidos
- novo #pedido: adiciona o #pedido
- cancela #pedido: remove o #pedido
-----------------------------------"""
sair = False
p=[]
while sair == False:
    e=input().split()
    if e[0] == "exibir":
        if len(p) == 0:
           print("sem pedidos")
        else:
           print("".join(p))
    if e[0] == "novo":
        p.append(e[1])
        print("pedido", e[1], "adicionado")
    if e[0] == "cancela":
        if e[1] not in p:
           print("pedido", p[1], "inexistente")
        else:
           p.remove(e[1])
           print("pedido", p[1], "removido")
    if e[0] == "ajuda":
        print(msg)

    e=e+1
    sair=True
    if e[0] == "sair":
        break
##########################################################################
msg = """-----------------------------------
Pizzaria 0.1 - menu de comandos
-----------------------------------
- ajuda: exibe o menu de ajuda
- sair: encerra o programa
- exibir: exibe a lista de pedidos
- novo #pedido: adiciona o #pedido
- cancela #pedido: remove o #pedido
-----------------------------------"""
pedidos = []

while (True):

    comandos = input().split()

    if comandos[0] == "exibir":
        if len(pedidos) == 0:
            print("sem pedidos")
        else:
            print(' '.join(pedidos))
            
    if comandos[0] == "novo":
        pedidos.append(comandos[1])
        print("pedido", comandos[1], "adicionado")
        
    if comandos[0] == "cancela":
        if comandos[1] not in pedidos:
            print("pedido", comandos[1], "inexistente")
        else:
            pedidos.remove(comandos[1])
            print("pedido", comandos[1], "removido")

    if comandos[0] == "sair":
        break
    
    if comandos[0] == "ajuda":
        print(msg)
