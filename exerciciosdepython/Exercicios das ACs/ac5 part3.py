def procurar(sequencia,caractere):
    quantidade = 0
    for x in sequencia:
        if x == caractere:
            quantidade = quantidade +1
    if quantidade == 0:
        print("Caractere nao encontrado.")
    else:
        print("O caractere buscado ocorre", quantidade, "vezes na sequencia.")
    
sequencia=input()
caractere=input()
procurar(sequencia,caractere)






    
