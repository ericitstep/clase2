def cuadrado_entero(valor):
    """
    Calcula el cuadrado de un valor flotante y lo convierte a entero usando la técnica de composición.

    Args:
        valor (float): El valor flotante al que se le calculará el cuadrado y se convertirá a entero.

    Retorna:
        int: El cuadrado del valor como un entero.

    Ejemplo:
    cuadrado_entero(2.5)
    """
    cuadrado = valor ** 2  # Calcula el cuadrado del valor
    entero = int(cuadrado)  # Convierte el cuadrado a entero usando la técnica de composición

    return entero

# Ejemplo de uso
valor_flotante = 2.5
resultado = cuadrado_entero(valor_flotante)
print(f"El cuadrado entero de {valor_flotante} es: {resultado}")
