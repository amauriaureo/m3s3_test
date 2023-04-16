class NameIsEmptyError(Exception):
    pass

class Paciente:
    def __init__(self, nome):
        self.paciente = nome
        # restante do código que inicializa os dados do paciente.