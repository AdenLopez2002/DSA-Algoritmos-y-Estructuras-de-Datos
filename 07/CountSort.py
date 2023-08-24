
def countSort(arr):                                            #2 ARREGLOS:
    output = [0 for i in range(len(arr))]     #uno del mismo tamaño que el original donde va guardanod el resultado
    count = [0 for i in range(10)]            #otro para contar, (del tamaño del elemento más grande dentro de mi arreglo)

    for i in arr:                            #cuantas veces aparece cada número
        count[i] +=1

    for i in range(1,10):                   #suma acumulativa
        count[i] += count[i-1]

    for i in range(len(arr)):               #ARREGLO RESULTADO:
        output[count[arr[i]]-1] = arr[i]    #Recorrer los números, extraer el indice del contador (restando 1) y asignarlo
        count[arr[i]] -= 1                  #decrementar
    return output
    

arr= [1 , 4, 1, 2, 7, 5, 2]
print("Original: ", arr)
print("Ordenado: ", countSort(arr))