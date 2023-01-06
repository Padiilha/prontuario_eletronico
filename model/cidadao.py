from model.domicilio import Domicilio
from model.pessoa import Pessoa


class Cidadao(Pessoa):
    def __init__(self, nome: str, cpf: str, cns: str):
        super().__init__(nome, cpf, cns)
        self.__domicilio = list()
        self.__historico_consultas = None

    def add_domicilio(self, domicilio: Domicilio):
        self.__domicilio.append(domicilio)

    def add_consulta(self):
        pass
