def fibonacci(n):
    """
    Calcula y devuelve el n-ésimo elemento de la serie de Fibonacci.

     Argumentos:
         n (int): El índice del elemento a recuperar.

     Devoluciones:
         int: El valor del n-ésimo elemento de la serie de Fibonacci.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
