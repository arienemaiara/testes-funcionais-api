import json
import os
import sys
import inspect

from Aluguel import Aluguel

VALOR_NOMINAL = 400

def test_depois_dia_30_AMR(): 
    aluguel = Aluguel(VALOR_NOMINAL, 31)
    valor = aluguel.calcular_valor()
    assert valor['valor_calculado'] == -1

def test_dia_invalido_AMR():
    aluguel = Aluguel(VALOR_NOMINAL, -1)
    valor = aluguel.calcular_valor()
    assert valor['valor_calculado'] == -1

def test_dia_1_a_5_AMR():
    for i in range(1, 6):
        aluguel = Aluguel(VALOR_NOMINAL, i)
        valor = aluguel.calcular_valor()
        valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1
        assert valor['valor_calculado'] == valor_aluguel

def test_dia_6_a_10_AMR():
    for i in range(6, 11):
        aluguel = Aluguel(VALOR_NOMINAL, i)
        valor = aluguel.calcular_valor()
        valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05
        assert valor['valor_calculado'] == valor_aluguel

def test_dia_11_a_15_AMR(): 
    for i in range(11, 16):
        aluguel = Aluguel(VALOR_NOMINAL, i)
        valor = aluguel.calcular_valor()
        assert valor['valor_calculado'] == VALOR_NOMINAL

def test_dia_16_AMR(): 
    aluguel = Aluguel(VALOR_NOMINAL, 16)
    valor = aluguel.calcular_valor()
    dias_atraso = 1
    multa_dias_atraso = dias_atraso * 0.001
    valor_aluguel = aluguel.valor_nominal + (aluguel.valor_nominal * 0.02) + (aluguel.valor_nominal * multa_dias_atraso)
    assert valor['valor_calculado'] == valor_aluguel