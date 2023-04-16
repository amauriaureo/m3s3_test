from paciente import Paciente, NameIsEmptyError

try:
    nome = input('Digite o nome do paciente: ')
    p = Paciente(nome)
