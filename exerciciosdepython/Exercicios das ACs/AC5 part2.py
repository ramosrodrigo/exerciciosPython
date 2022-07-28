def tabuada(r):
    for i in range(1,10,1):
        tabu = r*i
        print(r, "x", i ,"=", tabu)
    r=r+1
    print("")
    
n1=int(input())
while n1 < 1 or n1 > 9:
    print("Insira um número inicial entre 1 e 9")
    n1=int(input())

n2=int(input())
while n2 < 1 or n2 > 9:
    prin("Insira um número final entre 1 e 9")
    n2=int(input())
#para cada item da sequencia faça:    
for i in range(n1,n2,1):
    tabuada(i)
tabuada(n2)


#################################################################



    
n1=int(input())
n2=int(input())


if n2 < n1:
    print("Nenhuma tabuada nesse intervalo")
while n1 < 1 or n1 > 9:
    print("Insira um número inicial entre 1 e 9")
    n1=int(input())
while n2 < 1 or n2 > 9:
    print("Insira um número final entre 1 e 9")
    n2=int(input())    
while n1 >= 1 and n1 <=n2:
        if n2 <=9 and n2>= 1:
            for i in range(1,10,1):
                tabu = n1*i
                print(n1, "x", i ,"=", tabu)
            n1=n1+1 
            print("")    
        

###################FUNCIONOU#######################################
n1=int(input())
while n1 < 1 or n1 > 9:
    print("Insira um número inicial entre 1 e 9")
    n1=int(input())
    
n2=int(input())    
while n2 < 1 or n2 > 9:
    print("Insira um número final entre 1 e 9")
    n2=int(input())

if n2 < n1:
   print("Nenhuma tabuada nesse intervalo")
   
for x in range(n1,n2+1,1):
    for i in range(1,10,1):
        tabu = n1*i
        print(n1, "x", i ,"=", tabu)
    n1=n1+1 
    print("")            
        
        

        

    
