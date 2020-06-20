import json
import os
import sys
import inspect
currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from Aluguel import Aluguel

VALOR_NOMINAL = 400.0

##Dias inválidos
def test_dia_invalido_AMR():
    aluguel = Aluguel(VALOR_NOMINAL, 0)
    valor = aluguel.calcular_valor()
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(-1, valor['valor_calculado']))
    assert valor['valor_calculado'] == -1

def test_dia_31_AMR(): 
    aluguel = Aluguel(VALOR_NOMINAL, 31)
    valor = aluguel.calcular_valor()
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(-1, valor['valor_calculado']))
    assert valor['valor_calculado'] == -1

##Desconto 10%
def test_dia_1_AMR():
    aluguel = Aluguel(VALOR_NOMINAL, 1)
    valor = aluguel.calcular_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

def test_dia_3_AMR():
    aluguel = Aluguel(VALOR_NOMINAL, 3)
    valor = aluguel.calcular_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

def test_dia_5_AMR():
    aluguel = Aluguel(VALOR_NOMINAL, 5)
    valor = aluguel.calcular_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

##Desconto 5%
def test_dia_6_AMR():
    aluguel = Aluguel(VALOR_NOMINAL, 6)
    valor = aluguel.calcular_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

def test_dia_8_AMR():
    aluguel = Aluguel(VALOR_NOMINAL, 8)
    valor = aluguel.calcular_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

def test_dia_10_AMR():
    aluguel = Aluguel(VALOR_NOMINAL, 10)
    valor = aluguel.calcular_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

##Valor nominal
def test_dia_11_AMR(): 
    aluguel = Aluguel(VALOR_NOMINAL, 11)
    valor = aluguel.calcular_valor()
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(VALOR_NOMINAL, valor['valor_calculado']))
    assert valor['valor_calculado'] == VALOR_NOMINAL

def test_dia_12_AMR(): 
    aluguel = Aluguel(VALOR_NOMINAL, 12)
    valor = aluguel.calcular_valor()
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(VALOR_NOMINAL, valor['valor_calculado']))
    assert valor['valor_calculado'] == VALOR_NOMINAL

def test_dia_15_AMR(): 
    aluguel = Aluguel(VALOR_NOMINAL, 15)
    valor = aluguel.calcular_valor()
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(VALOR_NOMINAL, valor['valor_calculado']))
    assert valor['valor_calculado'] == VALOR_NOMINAL

##Multa
def test_multa_atraso_AMR(): 
    aluguel = Aluguel(VALOR_NOMINAL, 16)
    valor = aluguel.calcular_valor()
    dias_atraso = 1
    multa_dias_atraso = dias_atraso * 0.001
    valor_aluguel = aluguel.valor_nominal + (aluguel.valor_nominal * 0.02) + (aluguel.valor_nominal * multa_dias_atraso)
    sys.stderr.write("Valor esperado: {} - valor recebido {}".format(valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel