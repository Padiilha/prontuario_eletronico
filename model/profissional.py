from model.pessoa import Pessoa
from model.ubs import Ubs


class Profissional(Pessoa):
    def __init__(self, nome: str, cpf: str, cns: str, seq_profissional: int, cbo: str):
        super().__init__(nome, cpf, cns)
        self.__seq_profissional = seq_profissional
        self.__cbo = cbo
        self.__ubs = Ubs

    @property
    def seq_profissional(self) -> int:
        return self.__seq_profissional

    @property
    def cbo(self) -> str:
        return self.__cbo

    @cbo.setter
    def cbo(self, cbo: str):
        self.__cbo = cbo

    @property
    def ubs(self) -> Ubs:
        return self.__ubs

    @ubs.setter
    def ubs(self, ubs: Ubs):
        self.__ubs = ubs
