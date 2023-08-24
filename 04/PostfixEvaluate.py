from PostfixTranslate import *
from SimpleStack import *

def PostfixEvaluate(formula):  # Translate infix to Postfix and
                               # evaluate the result

   postfix = PostfixTranslate(formula) # Postfix string
   s = Stack(100)                      # Operand stack
   A=1
   B=A
   #A=(3 * 2) * A           #(A = 3 * 2) * A
   #PROBAR CON ESTO:: (A = 3 + 4 * 5) + (B = 7 * 6) + B/A   
   A = 3 + 4 * 5
   B = 7 * 6

   
   token, postfix = nextToken(postfix)
   while token:
      prec = precedence(token)  # Is it an operator?         
         
      if prec:                  # If input token is an operator
         right = s.pop()        # Get left and right operands
         left = s.pop()         # from stack
                  
         if token == '|':       # Perform operation and push
            s.push(left | right)
         elif token == '&':
            s.push(left & right)
         elif token == '+':
            s.push(left + right)
         elif token == '-':
            s.push(left - right)
         elif token == '*':            
            s.push(A)
            s.push(B)
            A*=A
            B*=B
         elif token == '/':
            s.push(A)
            s.push(B)
            A/=A
            B/=B
         elif token == '%':
            s.push(left % right)
         elif token == '^':
            s.push(left ^ right)
         elif token == '=' or token == ')' :         #Incluimos el igual
            s.push(A)
            s.push(B)
            
               
      elif token!=prec:         
         s.push(token)
         #if token!='A' or token != 'B':
            #print("Error: Variable indefinida.")
         
      else:                     # Else token is operand
         s.push(int(token))     # Convert to integer and push
                  
         
      print('After processing', token, 'stack holds:', s)
        
      token, postfix = nextToken(postfix) # Fencepost loop

   print('Final result =', s.pop()) # At end of input, print result

if __name__ == '__main__':
   infix_expr = input("Infix expression to evaluate: ")
   print("The postfix representation of", infix_expr, "is:",
         PostfixTranslate(infix_expr))
   PostfixEvaluate(infix_expr)
