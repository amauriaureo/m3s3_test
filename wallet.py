class InsufficientAmount(Exception):
     pass


class Wallet(object):

     def __init__(self, quantidade_inicial=0):
          self.saldo = quantidade_inicial


     def spend_cash(self, quantidade):
          if self.saldo < quantidade:
               raise InsufficientAmount(f'Não há o suficiente disponível para gastar {quantidade}')
          self.saldo -= quantidade


     def add_cash(self, quantidade):
          self.saldo += quantidade
