import Array

maxSize = 10 # Max size of the array

arr = Array.Array(maxSize) # Create an array object

arr.insert(77) # Insert 10 items
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Setting item at index 3 to 33")
arr.set(3, 33)

print("Array after deletions has", len(arr), "items")
arr.traverse()


#INCISO 2.1
print("\n*Buscar número mayor*")
max=arr.getMaxNum()
print("El mayor es: %s " % (max))
arr.delete(max) #INCISO 2.2 (Borra el número mayor de la lista)
arr.traverse()

#INCISO 2.3 Clasificar el arreglo utilizando "sorted()"

print("\nMatriz desordenada:")
arr.traverse()

arr_clasificado = []
arr.traverse(lambda item: arr_clasificado.append(item))

arr_clasificado_numerico = [item for item in arr_clasificado if isinstance(item, (int, float))]
arr_clasificado_letras = [item for item in arr_clasificado if isinstance(item, str)]

arr_clasificado_numerico = sorted(arr_clasificado_numerico)
arr_clasificado_letras = sorted(arr_clasificado_letras)

arr_clasificado_ordenado = arr_clasificado_numerico + arr_clasificado_letras

print("\nMatriz ordenada:")
for item in arr_clasificado_ordenado:
    print(item)


#INCISO 2.5
import OrderedRecordArray

mSize =12
listaord = OrderedRecordArray.OrderedRecordArray(mSize) #creamos lista1
lista = OrderedRecordArray.OrderedRecordArray(6)
lista2= OrderedRecordArray.OrderedRecordArray(6)

print("Creamos la lista 1: ")
lista.randomfill()
print("Creamos la lista 2: ")
lista2.randomfill()
#Aplicamos el merge

print("El arreglo ordenado sería:%s " % (merge(lista,lista2)))





