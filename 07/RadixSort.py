def radixSort(arr):
    max1 = max(arr)

    exp= 1
    while max1 / exp >= 1:
        countSort(arr,exp)
        exp*=10


def countSort(arr, exp1):        #exp1=unidad de enfoque
    output = [0]*(len(arr))    
    count = [0]*(10)                #solo de 0 al 9

    for i in range(0, len(arr)):
        index = arr[i] // exp1      #extraemos, dividimos entero y mod 10 
        count[index %10] +=1         
        

    for i in range(1,10):                   #suma acumulativa
        count[i] += count[i-1]
        

    i= len(arr)-1
    while i >= 0:
        index= arr[i] // exp1
        output[count[index % 10] - 1]= arr[i]
        count[index % 10]-=1
        i-=1

    i=0
    for i in range(len(arr)):               
        arr[i]=output[i]


arr = [170, 45, 75, 90, 802, 24, 2, 66]
print ("Original: ", arr)
print ("Ordenado: ",end=" ")
radixSort(arr)
 
for i in range(len(arr)):
    print(arr[i],end=", ")
 
    

