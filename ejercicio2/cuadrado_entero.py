# Códifique un algoritmo en python que tome como argumento un valor
# flotante, obtenga su cuadrado y lo convierta a entero usando la técnica de
# composición.

# Calcula el cuadrado de un valor flotante y lo convierte a entero usando la técnica de composición.

    # Args:
    #     valor (float): El valor flotante al que se le calculará el cuadrado y se convertirá a entero.

    # Retorna:
    #     int: El cuadrado del valor como un entero.

    # Ejemplo:
    # cuadrado_entero(2.5)

def cuadradoEntero(valor):
     
    cuadrado = valor ** 2  # Calcula el cuadrado del valor
    entero = int(cuadrado)  # Convierte el cuadrado a entero usando la técnica de composición

    return entero

# Ejemplo de uso
valorFlotante = 2.5
resultado = cuadradoEntero(valorFlotante)
print(f"El cuadrado entero de {valorFlotante} es: {resultado}")
