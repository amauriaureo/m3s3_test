# from exercicio1 import calculo_desconto
import pytest


def calculo_desconto(valor_unitario, quantidade):
    desconto = 1

    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    valor_com_desconto = valor_unitario * desconto * quantidade
    # valor_sem_desconto = valor_unitario * quantidade
    return valor_com_desconto


def test_calculo_desconto_qtd_menor_que_10():
    assert calculo_desconto(10, 3) == 30


def test_calculo_desconto_qtd_maior_que_10():
    assert calculo_desconto(10, 50) == 475


def test_calculo_desconto_qtd_maior_que_100():
    assert calculo_desconto(10, 111) == 999


def test_calculo_desconto_qtd_maior_que_1000():
    assert calculo_desconto(10, 2000) == 17000
