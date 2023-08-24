# Binary Tree
class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key     # self.data = key

class ExpressionTress():
    def __init__(self):
            self.root=None
            #Implementation
            tree = [None] * 10

    def Inorder(root):
        if root:
            Inorder(root.left)      #recursivo
            print(root.val, end=" ")
            Inorder(root.right)
            
    def Preorder(root):
        if root:
            print(root.val, end=" ")
            Preorder(root.left)
            Preorder(root.right)
            
    def Postorder(root):
        if root:
            Postorder(root.left)
            Postorder(root.right)
            print(root.val, end=" ")




    def root(key):      #redefine el arbol cada vez que llama a root
        tree[0]=key

    def set_left(key, parent):
        if tree[parent] == None:
            print("Parent not found!")
        else:
            tree[(parent * 2) + 1] = key        #formula (i*2)+1 es el left del padre


    def set_right(key, parent):
        if tree[parent] == None:
            print("Parent not found!")
        else:
            tree[(parent * 2) + 2] = key        #formula (i*2)+2 es el right del padre


#Imprimir
    def print_tree():
        for i in range(10):
            if tree[i]:
                print(tree[i], end = " ")
            else:
                print("-", end = " ")
        print()



#Expression Trees desde un POST-FIX
    def isOperator(c):      #función que recionoce los operadores
        if ( c=='+' or
        c == '-' or
        c == '*' or
        c == '/' or
        c == '^'):
            return True
        else:
            return False

    def constructTree(postfix):
        stack = []
        for char in postfix:
            
            t = Node(char)          #crea nodo
            
            if isOperator(char):        #checa si es operador
                t1 = stack.pop()
                t2 = stack.pop()                
                t.right = t1
                t.left = t2
                
            stack.append(t)
        t = stack.pop()
        return t
    
    #def constructTree(postfix):
        #stack = []
        #print("Postfix Expression is :  " + postfix)
        for char in postfix:
            #print("Read " + char + " and created a node...")
            t = Node(char)
            if isOperator(char):                        #chequea si es un operador
                #print(char + " is an operator...")
                t1 = stack.pop()
                #print("Popped() " + t1.val )
                t2 = stack.pop()
                #print("Popped() " + t2.val )
                t.right = t1
                t.left = t2    
            #else:
                #print(char + " is an operand...")
            stack.append(t)
            #print("Push() " +  t.val + " into the stack...")
        t = stack.pop()
        #print("Popped() " + t.val )
        return t

postfix = "ab+ef*g*-"
r = constructTree(postfix)
Inorder(r)







"""
root('A')
set_left('B', 0)
set_right('C', 0)

set_left('D', 1)
set_right('E', 1)

set_left('F', 2)
set_right('G', 2)

print_tree()"""



