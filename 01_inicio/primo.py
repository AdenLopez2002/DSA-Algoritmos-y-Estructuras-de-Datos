num=int (input("Ingrese un número: "))

if num%2 != 0:
    print ("Si es primo.")
else:
    print ("No es primo." ,"\n\n", "Factores:")

    primos=[] #creamos una lista vacía

    for i in range(2, num): 
        while num % i == 0:
            primos.append(i) #anexandolos a la lista
            num= num / i
            
    print (primos)
    
