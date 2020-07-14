import pytest
import sys
import os
import inspect
import csv
currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from Aluguel import Aluguel

VALOR_NOMINAL = 400.0
CENARIOS = [(0,-1), (1,360.0), (2,360.0), (4,360.0),(5,360.0),(6,380.0),(7,380.0),(9,380.0),(10,380.0),(11,400.0),(12,400.0),(14,400.0),(15,400.0),(16,408.4),(17,408.8),(29,413.6),(30,414.0),(31,-1)]

### Parametrizando os testes
@pytest.mark.parametrize('dia, valor_esperado', CENARIOS)
def test_cenarios(dia, valor_esperado):
    aluguel = Aluguel(VALOR_NOMINAL, dia)
    resultado = aluguel.calcular_valor()
    valor_aluguel = resultado['valor_calculado']
    sys.stderr.write("Dia {} - Valor esperado: {} - valor recebido: {}".format(dia, valor_esperado, valor_aluguel))
    assert valor_aluguel == valor_esperado