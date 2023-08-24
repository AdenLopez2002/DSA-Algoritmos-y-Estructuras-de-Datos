from OrderedRecordArray import*

def second(x):
    return x[1]
    
maxSize = 1000 # Max size of the array
arr = OrderedRecordArray(maxSize, second) # Create the array object
        
# Insert 10 items
for rec in [('a', 3.1), ('b', 7.5), ('c', 6.0), ('d', 3.1),
            ('e', 1.4), ('f', -1.2), ('g', 0.0), ('h', 7.5),
            ('i', 7.5), ('j', 6.0)]:
     arr.insert(rec)

print("Array containing", len(arr), "items:\n", arr)

#Merge
import random
print ("\nMerge():")
for rec2 in [('A', round(random.uniform(-1,10),1)), ('B', round(random.uniform(-1,10),1)), ('C',round(random.uniform(-1,10),1)),
             ('D',round(random.uniform(-1,10),1)), ('E', round(random.uniform(-1,10),1)), ('F', round(random.uniform(-1,10),1)),
             ('G', round(random.uniform(-1,10),1)), ('H', round(random.uniform(-1,10),1)), ('I', round(random.uniform(-1,10),1)),
             ('J', round(random.uniform(-1,10),1))]:
    arr.insert(rec2)

     
print("\nArray merged contiene ", len(arr), "items: \n", arr, "\n\n")
     
       
# Delete a few items, including some duplicates
for rec in [('c', 6.0), ('g', 0.0), ('g', 0.0), ('b', 7.5),('i', 7.5)]:
    print("Deleting", rec, "returns", arr.delete(rec))
        
print("Array after deletions has", len(arr), "items:\n", arr)

        
for key in [4.4, 6.0, 7.5]:
    print("find(", key, ") returns", arr.find(key),"and get(", arr.find(key), ") returns",
    arr.get(arr.find(key)))


