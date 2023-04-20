import pytest
from exercicio3 import ler_dimensoes_objeto, calcular_preco_volume, validar_medida, ler_peso_objeto, calcular_multiplicador_peso, ler_rota, calcular_multiplicador_rota, calcular_frete, gerar_codigo, cadastrar_peca, imprimir_peca, consultar_pecas, remover_peca


@pytest.fixture
def dimensoes():
    ler_dimensoes_objeto()


class Calcular:
    def preco_volume():
        calcular_preco_volume(volume)

    def multiplicador_peso():
        calcular_multiplicador_peso(peso)

    def multiplicador_rota():
        calcular_multiplicador_rota(rota)

    def frete():
        calcular_frete(volume, multiplicador_peso, multiplicador_rota)


class Peca:
    def cadastrar():
        cadastrar_peca()

    def imprimir():
        imprimir_peca(peca)

    def consultar():
        consultar_pecas()

    def remover():
        remover_peca()
