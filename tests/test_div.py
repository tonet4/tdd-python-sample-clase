# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import div

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación dividir
    def test_div(self):
        assert div(5,5) == -1
        assert div(10,2) == 5
        assert div(7,7) == 1
        assert div(24,12) == 2