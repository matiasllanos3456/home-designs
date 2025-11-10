"""
Tests para el módulo de combinaciones.

Este archivo contiene pruebas unitarias para verificar el correcto
funcionamiento del módulo combinaciones.py
"""

import unittest
from combinaciones import encontrar_combinaciones, contar_combinaciones


class TestCombinaciones(unittest.TestCase):
    """Pruebas unitarias para las funciones de combinaciones."""
    
    def test_combinaciones_5_elementos_2_en_2(self):
        """Prueba que 5 elementos tomados de 2 en 2 generan 10 combinaciones."""
        lista = [1, 2, 3, 4, 5]
        resultado = encontrar_combinaciones(lista, 2)
        
        # Verificar que se generan exactamente 10 combinaciones
        self.assertEqual(len(resultado), 10)
        
        # Verificar que todas son tuplas de 2 elementos
        for combo in resultado:
            self.assertEqual(len(combo), 2)
        
        # Verificar algunas combinaciones específicas
        self.assertIn((1, 2), resultado)
        self.assertIn((1, 5), resultado)
        self.assertIn((4, 5), resultado)
    
    def test_combinaciones_sin_repeticion(self):
        """Verifica que no hay repeticiones en las combinaciones."""
        lista = [1, 2, 3, 4, 5]
        resultado = encontrar_combinaciones(lista, 2)
        
        # Convertir a set para verificar unicidad
        resultado_set = set(resultado)
        self.assertEqual(len(resultado), len(resultado_set))
    
    def test_orden_no_importa(self):
        """Verifica que (1,2) y (2,1) no aparecen ambas (combinaciones, no permutaciones)."""
        lista = [1, 2, 3]
        resultado = encontrar_combinaciones(lista, 2)
        
        # Si (1,2) está, (2,1) no debería estar
        if (1, 2) in resultado:
            self.assertNotIn((2, 1), resultado)
    
    def test_combinaciones_con_letras(self):
        """Prueba que funciona con letras."""
        letras = ['A', 'B', 'C', 'D', 'E']
        resultado = encontrar_combinaciones(letras, 2)
        
        self.assertEqual(len(resultado), 10)
        self.assertIn(('A', 'B'), resultado)
        self.assertIn(('D', 'E'), resultado)
    
    def test_combinaciones_3_en_3(self):
        """Prueba combinaciones de 5 elementos tomados de 3 en 3."""
        lista = [1, 2, 3, 4, 5]
        resultado = encontrar_combinaciones(lista, 3)
        
        # C(5,3) = 10
        self.assertEqual(len(resultado), 10)
        
        # Verificar que todas son tuplas de 3 elementos
        for combo in resultado:
            self.assertEqual(len(combo), 3)
    
    def test_contar_combinaciones_formula(self):
        """Verifica que la fórmula matemática funciona correctamente."""
        # C(5,2) = 10
        self.assertEqual(contar_combinaciones(5, 2), 10)
        
        # C(5,3) = 10
        self.assertEqual(contar_combinaciones(5, 3), 10)
        
        # C(10,2) = 45
        self.assertEqual(contar_combinaciones(10, 2), 45)
        
        # C(4,2) = 6
        self.assertEqual(contar_combinaciones(4, 2), 6)
    
    def test_lista_vacia(self):
        """Prueba con lista vacía."""
        resultado = encontrar_combinaciones([], 2)
        self.assertEqual(len(resultado), 0)
    
    def test_r_mayor_que_n(self):
        """Prueba cuando r es mayor que el tamaño de la lista."""
        lista = [1, 2, 3]
        resultado = encontrar_combinaciones(lista, 5)
        self.assertEqual(len(resultado), 0)
    
    def test_consistencia_contar_y_generar(self):
        """Verifica que el conteo matemático coincide con las combinaciones generadas."""
        for n in range(3, 8):
            for r in range(1, n + 1):
                lista = list(range(1, n + 1))
                resultado = encontrar_combinaciones(lista, r)
                esperado = contar_combinaciones(n, r)
                self.assertEqual(len(resultado), esperado,
                               f"C({n},{r}) debería ser {esperado}, pero se generaron {len(resultado)}")


if __name__ == '__main__':
    print("Ejecutando pruebas unitarias para combinaciones.py")
    print("=" * 60)
    unittest.main(verbosity=2)
