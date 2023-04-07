import pytest
from wallet import Wallet


def test_saldo_inicial():
    carteira = Wallet()
    assert carteira.saldo == 0
