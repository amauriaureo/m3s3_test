from paciente import Paciente, NameIsEmptyError

try:
    nome = input('Digite o nome do paciente: ')
    p = Paciente(nome)
except TypeError:
    print('O nome deve ser uma string. Tente novamente...')
except NameIsEmptyError:
    print('O nome não poder ser uma string vazia. Preencha uma valor...')
except Exception as e:
    print('Ocorreu um erro inesperado ao criar o objeto de Paciente.')
    print('informações do erro: ', e)
