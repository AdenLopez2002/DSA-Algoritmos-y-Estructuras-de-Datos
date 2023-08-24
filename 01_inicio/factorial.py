def factorial(n):   #5
    if n==0:
        return 1
    else:
        recursivo = factorial(n-1) #Esta es la parte recursiva #5-1 = 4
        resultado = n*recursivo #5*4!
        print (resultado)
    return resultado


n = int(input("Introduce un número entero positivo: "))
factorial(n)
