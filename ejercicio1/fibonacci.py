# Códifique una función que usando la técnica de recursividad imprima el
# enesimo elemento de la serie de fibonacci.

# Calcula y devuelve el n-ésimo elemento de la serie de Fibonacci.

    #  Argumentos:
    #      n (int): El índice del elemento a recuperar.

    #  Devoluciones:
    #      int: El valor del n-ésimo elemento de la serie de Fibonacci.
def fibonacci(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
