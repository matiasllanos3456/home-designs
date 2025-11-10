# Combinaciones en Python

## Descripción

Este módulo proporciona una **forma eficiente** de hallar las posibles combinaciones de juntar una lista de 5 elementos de 2 en 2 sin repetición en Python.

## Solución

La solución utiliza el módulo `itertools.combinations` de Python, que es la forma más eficiente de generar combinaciones sin repetición. Esta implementación tiene una complejidad de tiempo óptima y es parte de la biblioteca estándar de Python.

## Archivos

- **combinaciones.py**: Módulo principal con las funciones para generar combinaciones
- **test_combinaciones.py**: Pruebas unitarias para verificar el correcto funcionamiento

## Uso

### Ejemplo Básico

```python
from combinaciones import encontrar_combinaciones

# Lista de 5 elementos
elementos = [1, 2, 3, 4, 5]

# Encontrar combinaciones de 2 en 2
combinaciones = encontrar_combinaciones(elementos, 2)

print(combinaciones)
# Salida: [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
```

### Ejecutar el Script de Demostración

```bash
python3 combinaciones.py
```

Este comando mostrará varios ejemplos incluyendo:
- Combinaciones de números (1-5) tomados de 2 en 2
- Combinaciones de letras (A-E) tomados de 2 en 2
- Demostración con lista más grande (20 elementos)

### Ejecutar las Pruebas

```bash
python3 test_combinaciones.py
```

## Funciones Principales

### `encontrar_combinaciones(lista, r=2)`

Encuentra todas las combinaciones posibles de una lista tomando r elementos a la vez.

**Parámetros:**
- `lista`: Lista de elementos para combinar
- `r`: Número de elementos a tomar en cada combinación (por defecto 2)

**Retorna:**
- Lista de tuplas con todas las combinaciones posibles

### `contar_combinaciones(n, r)`

Calcula el número de combinaciones posibles usando la fórmula matemática C(n, r) = n! / (r! * (n-r)!)

**Parámetros:**
- `n`: Número total de elementos
- `r`: Número de elementos a tomar en cada combinación

**Retorna:**
- Número de combinaciones posibles

## Resultado para 5 Elementos de 2 en 2

Para una lista de 5 elementos tomados de 2 en 2, se generan **10 combinaciones únicas**:

1. (1, 2)
2. (1, 3)
3. (1, 4)
4. (1, 5)
5. (2, 3)
6. (2, 4)
7. (2, 5)
8. (3, 4)
9. (3, 5)
10. (4, 5)

## Complejidad

- **Tiempo**: O(C(n,r)) donde C(n,r) es el coeficiente binomial
- **Espacio**: O(C(n,r)) para almacenar todas las combinaciones

Para el caso específico de 5 elementos tomados de 2 en 2:
- C(5,2) = 10 combinaciones
- Complejidad: O(10)

## Por Qué Es Eficiente

1. **Usa la biblioteca estándar**: `itertools.combinations` está implementado en C, lo que lo hace muy rápido
2. **No genera duplicados**: Solo genera combinaciones únicas
3. **Orden correcto**: No genera permutaciones, solo combinaciones (no repetición de pares en diferente orden)
4. **Memoria eficiente**: Puede usarse como iterador sin almacenar todas las combinaciones en memoria si es necesario

## Ejemplo Alternativo (Sin Itertools)

Si bien `itertools.combinations` es la solución más eficiente, también se podría implementar manualmente:

```python
def combinaciones_manual(lista, r):
    """Implementación manual de combinaciones (menos eficiente)."""
    def generar(inicio, combo_actual):
        if len(combo_actual) == r:
            resultado.append(tuple(combo_actual))
            return
        
        for i in range(inicio, len(lista)):
            generar(i + 1, combo_actual + [lista[i]])
    
    resultado = []
    generar(0, [])
    return resultado
```

Sin embargo, se recomienda usar `itertools.combinations` por su eficiencia y confiabilidad.
