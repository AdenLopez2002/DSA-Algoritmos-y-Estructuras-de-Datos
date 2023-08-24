def fibonacci(n):   #6/6/23
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        resultado = fibonacci(n-1) + fibonacci(n-2)
        print (resultado)
        return resultado
    else:
        print("Debe ingresar un número positivo.")
        return -1        
    

n = int(input("Introduzca un número entero positivo: "))
fibonacci(n)
