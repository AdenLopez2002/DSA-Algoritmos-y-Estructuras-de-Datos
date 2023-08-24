#2.1

class Array(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize #guarda el arreglo como una lista

        self.__nItems = 0 #no hay elementos en el arreglo todavía

    def __len__(self):
        return self.__nItems #retorna el numero de elementos
    
    def get(self, n):
        if n>=0 and n< self.__nItems: #chequea si el numero n está en os limites
            return self.__a[n]

    def set(self, n, value):
        if n>=0 and n< self.__nItems: #chequea si el numero n está en os limites
            self.__a[n] = value  #aqui hace el set

    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems +=1

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j]==item:
                return j
        return -1

    def search(self, item):
        return self.get(self.find(item))

    def delete(self, item):
        for j in range(self.__nItems): # of an item
            if self.__a[j] == item: # Found item
                self.__nItems -= 1 # One fewer at end
                for k in range(j, self.__nItems): # Move items from
                     self.__a[k] = self.__a[k+1]
                return True
        return False

    def traverse(self, function=print): 
         for j in range(self.__nItems):
             function(self.__a[j])


    
    def getMaxNum(self): #self es porque esta dentro del objeto
        if (self.__nItems)!=0:
            print("Si hay elementos")
            max_value= 0 
            print(max_value)#metodo
            
            for x in range(self.__nItems):                
                if isinstance(self.__a[x], (int, float)) and self.__a[x]>max_value:
                    max_value = self.__a[x]                
            print (max_value)
            return max_value
        
        elif self.__nItems==0:
            print("No hay elementos.")
            return [None]
    
"""Inciso 2.1:

        En la clase arreglo, agregar un método que retorne el número más
        alto del arreglo o NONE, si en el arreglo no hay números """
        


