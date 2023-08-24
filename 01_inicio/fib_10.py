def fib(n):         #método de fibonacci
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
        

def imprimir(x):    #para imprimir
    print ("\t",fib(x-2), " + ", fib(x-1), " = ", fib(x))
    
        
        
print("SERIE DE FIBONACCI: ---Viendo los sumandos")    
y=1
n=int(input("Ingrese un numero: "))

for x in range(n):
    if x< 2:
        print ("\nVuelta:",(y))
        print (fib(x)) #devuelve 0 ó 1
        y+=1
    elif x==2:
        print ("\nVuelta:",(y))
        imprimir(x) #imprime el método
        y+=1
    else:
        print ("\nVuelta:",(y))
        imprimir(x) #imprime el método
        print("\n...",fib(x-2), " y ", fib(x-1), " salen de:")
        
        #aqui se imprimen los factores
        for p in range(y-3):
            imprimir((x-p)-1)         
        y+=1
        

