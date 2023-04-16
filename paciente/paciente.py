class NameIsEmptyError(Exception):
    pass


class Paciente:
    def __init__(self, nome):
        self.paciente = nome
        # restante do código que inicializa os dados do paciente.

    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, nome):
        if not isinstance(nome, str):
            raise TypeError("'nome' inválido")
        if nome == '':
            raise NameIsEmptyError("'nome' é obrigatório")
        self._paciente = nome
