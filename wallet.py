class InsufficientAmount(Exception):
     pass


class Wallet(object):

     def __init__(self, quantidade_inicial=0):
          self.saldo = quantidade_inicial
          self.auditoria = list()


     def spend_cash(self, quantidade):
          if self.saldo < quantidade:
               self.auditoria.append(f"suspend spend {quantidade}")
               raise InsufficientAmount(f'Não há o suficiente disponível para gastar {quantidade}')
          self.auditoria.append(f"spend {quantidade}")
          self.saldo -= quantidade


     def add_cash(self, quantidade):
          self.auditoria.append(f"Add {quantidade}")
          self.saldo += quantidade
