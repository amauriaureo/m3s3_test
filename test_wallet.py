import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def carteira():
    return Wallet(10)


class TestSaldoInicial:
    def test_saldo_inicial_sem_parametro(self):
        carteira = Wallet()
        assert carteira.saldo == 0

    def test_saldo_inicial_com_parametro(self, carteira):
        assert carteira.saldo == 10


class TestAdicionaSaldo:
    def test_adiciona_saldo(self, carteira):
        carteira.add_cash(10)
        assert carteira.saldo == 20


class TestRetiraSaldo:
    def test_retirar_da_carteira_com_saldo(self, carteira):
        carteira.spend_cash(10)
        assert carteira.saldo == 0

    def test_retirar_da_carteira_sem_saldo_suficiente(self, arteira):
        # carteira.spend_cash(10)
        # assert carteira.saldo == 0
        with pytest.raises(InsufficientAmount):
            carteira.spend_cash(20)

    def test_retira_da_carteira_parte_do_saldo(self, carteira):
        carteira.spend_cash(5)
        assert carteira.saldo == 5
