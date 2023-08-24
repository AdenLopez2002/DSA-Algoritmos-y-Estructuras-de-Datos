def triangular_explicado(nth):
    print("Estamos sacando el valor n del índice # ", nth)
    if nth < 1:
        print("CASO BASE. Retorna 0")
        return 0

    valor = nth + triangular_explicado(nth-1)
    print("Para el número #", nth, "retornamos", valor)
    return(valor)

print("///SERIE TRIANGULAR///")
#nth= int(input("Ingrese el valor"))
triangular_explicado(237)



""" con ciclos
def triangular_loop(nth): 
    total = 0 
    for n in range(nth, 0, -1): 
        total += n 
    return total
    """
