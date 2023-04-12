import pytest
from wallet import Wallet


def test_saldo_inicial_sem_parametro():
    carteira = Wallet()
    assert carteira.saldo == 0


def test_saldo_inicial_com_parametro():
    carteira = Wallet(10)
    assert carteira.saldo == 10


def test_adiciona_saldo():
    carteira = Wallet(10)
    carteira.add_cash(10)
    assert carteira.saldo == 20
