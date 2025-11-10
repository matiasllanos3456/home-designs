"""
Módulo para encontrar combinaciones de elementos sin repetición.

Este módulo proporciona una forma eficiente de hallar las posibles combinaciones
de juntar una lista de elementos de 2 en 2 sin repetición usando itertools.
"""

from itertools import combinations


def encontrar_combinaciones(lista, r=2):
    """
    Encuentra todas las combinaciones posibles de una lista tomando r elementos a la vez.
    
    Esta función utiliza itertools.combinations que es la forma más eficiente
    de generar combinaciones sin repetición en Python.
    
    Args:
        lista: Lista de elementos para combinar
        r: Número de elementos a tomar en cada combinación (por defecto 2)
    
    Returns:
        Lista de tuplas con todas las combinaciones posibles
    
    Ejemplo:
        >>> encontrar_combinaciones([1, 2, 3, 4, 5], 2)
        [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    """
    return list(combinations(lista, r))


def contar_combinaciones(n, r):
    """
    Calcula el número de combinaciones posibles usando la fórmula matemática.
    
    Fórmula: C(n, r) = n! / (r! * (n-r)!)
    
    Args:
        n: Número total de elementos
        r: Número de elementos a tomar en cada combinación
    
    Returns:
        Número de combinaciones posibles
    
    Ejemplo:
        >>> contar_combinaciones(5, 2)
        10
    """
    from math import factorial
    return factorial(n) // (factorial(r) * factorial(n - r))


if __name__ == "__main__":
    # Ejemplo con una lista de 5 elementos, combinados de 2 en 2
    print("=" * 60)
    print("COMBINACIONES DE 5 ELEMENTOS TOMADOS DE 2 EN 2")
    print("=" * 60)
    
    # Lista de ejemplo con 5 elementos
    elementos = [1, 2, 3, 4, 5]
    
    print(f"\nLista original: {elementos}")
    print(f"Tomando elementos de: 2 en 2")
    
    # Encontrar todas las combinaciones
    combis = encontrar_combinaciones(elementos, 2)
    
    print(f"\nNúmero total de combinaciones: {len(combis)}")
    print(f"(Verificación matemática: C(5,2) = {contar_combinaciones(5, 2)})")
    
    print("\nCombinaciones encontradas:")
    for i, combo in enumerate(combis, 1):
        print(f"  {i:2d}. {combo}")
    
    # Ejemplo adicional con letras
    print("\n" + "=" * 60)
    print("EJEMPLO ADICIONAL CON LETRAS")
    print("=" * 60)
    
    letras = ['A', 'B', 'C', 'D', 'E']
    combis_letras = encontrar_combinaciones(letras, 2)
    
    print(f"\nLista de letras: {letras}")
    print(f"Combinaciones: {combis_letras}")
    
    # Demostración de eficiencia con lista más grande
    print("\n" + "=" * 60)
    print("DEMOSTRACIÓN DE EFICIENCIA")
    print("=" * 60)
    
    lista_grande = list(range(1, 21))  # 20 elementos
    combis_grande = encontrar_combinaciones(lista_grande, 2)
    
    print(f"\nLista de 20 elementos: 1 al 20")
    print(f"Combinaciones posibles de 2 en 2: {len(combis_grande)}")
    print(f"(Cálculo: C(20,2) = {contar_combinaciones(20, 2)})")
    print(f"\nPrimeras 5 combinaciones: {combis_grande[:5]}")
    print(f"Últimas 5 combinaciones: {combis_grande[-5:]}")
