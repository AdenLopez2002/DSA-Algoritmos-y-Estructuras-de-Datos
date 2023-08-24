import heapq
from collections import Counter

class Node():
    def __init__(self, ch, freq):        
        self.left = None
        self.right = None
        self.ch = ch        #caracter
        self.freq = freq    #frecuencia del caracter

    def __lt__(self, other):
        return self.freq < other.freq       #menos frecuente y mas frecuente
    

def build_tree(text):
    counter = Counter(text)                             #contador de texto
    pq = [Node(ch, counter[ch]) for ch in counter]      #usamos un  Priority queue, para hacer POP  con prioridad a los elementos 
                                                        #con menor frecuencia a repetirse                                  
    heapq.heapify(pq)
    
    while len(pq) > 1:
        left = heapq.heappop(pq)        #hijos izq y der
        right = heapq.heappop(pq)
        parent = Node(None, left.freq + right.freq)
        heapq.heappush(pq, parent)          #Push al queue
    return heapq.heappop(pq)                #retorna un pop de los elementos


def build_map(root):
    def dfs(root, code, encoding_map):
        if root.ch:
            encoding_map[root.ch] = ''.join(code)
        else:
            code.append('0')
            dfs(root.left, code, encoding_map)
            code.pop()
            code.append('1')
            dfs(root.right, code, encoding_map)
            code.pop()
    encoding_map = {}
    dfs(root, [], encoding_map)
    return encoding_map


def encode(text):
    root = build_tree(text)
    encoding_map = build_map(root)
    return ''.join([encoding_map[ch] for ch in text])


def decode(encoded, root):
    if root.ch:
        return root.ch * len(encoded)
    decoded = []
    node = root
    for bit in encoded:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.ch:
            decoded.append(node.ch)
            node = root
    return ''.join(decoded)

text=("BANANA")
print(build_tree(text))