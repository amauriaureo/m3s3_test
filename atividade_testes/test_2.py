import pytest


# class Cardapio():
def pedido_lanchonete(codigo):
    # self.codigo = codigo
    # self.total = total
    total = 0

    # while True:
    if codigo == 100:
        print('Você pediu um Cachorro Quente no valor de 9,00')
        total += 9.00
    elif codigo == 101:
        print('Você pediu um Cachorro Quente Duplo no valor de 11,00')
        total += 11.00
    elif codigo == 102:
        print('Você pediu um X-Egg no valor de 12,00')
        total += 12.00
    elif codigo == 103:
        print('Você pediu um X-Salada no valor de 12,00')
        total += 12.00
    elif codigo == 104:
        print('Você pediu um X-Bacon no valor de 14,00')
        total += 14.00
    elif codigo == 105:
        print('Você pediu um X-Tudo no valor de 17,00')
        total += 17.00
    elif codigo == 200:
        print('Você pediu um Refrigerante Lata no valor de 5,00')
        total += 5.00
    elif codigo == 201:
        print('Você pediu um Chá Gelado no valor de 4,00')
        total += 4.00
    else:
        print('Opção inválida')
        # codigo = int(input('Entre com o código desejado: '))

    return total


def cachorro_quente():
    assert pedido_lanchonete(100) == 9.00


def cachorro_quente_duplo():
    assert pedido_lanchonete(101) == 11.00


def x_egg():
    assert pedido_lanchonete(102) == 12.00


def x_salada():
    assert pedido_lanchonete(103) == 12.00


def x_bacon():
    assert pedido_lanchonete(104) == 14.00


def x_tudo():
    assert pedido_lanchonete(105) == 17.00


def refri():
    assert pedido_lanchonete(106) == 5.00


def cha_gelado():
    assert pedido_lanchonete(107) == 4.00
