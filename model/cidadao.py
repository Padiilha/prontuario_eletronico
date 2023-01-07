from model.consulta import Consulta
from model.domicilio import Domicilio
from model.pessoa import Pessoa


class Cidadao(Pessoa):
    def __init__(self, nome: str, cpf: str, cns: str, seq_cidadao: int):
        super().__init__(nome, cpf, cns)
        self.__seq_cidadao = seq_cidadao
        self.__domicilio = list()

    @property
    def seq_cidadao(self) -> int:
        return self.__seq_cidadao

    def add_domicilio(self, domicilio: Domicilio):
        self.__domicilio.append(domicilio)

    def add_consulta(self, consulta: Consulta):
        super().add_consulta(consulta)
