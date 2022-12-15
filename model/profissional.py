from model.pessoa import Pessoa


class Profissional(Pessoa):
    def __init__(self, nome: str, cpf: str, cns: str, seq_profissional: int, cbo: str):
        super().__init__(nome, cpf, cns)
        self.__seq_profissional = seq_profissional
        self.__cbo = cbo
        self.__ubs = None
        self.__historico_atendimentos = None

    @property
    def cbo(self) -> str:
        return self.__cbo

    @cbo.setter
    def cbo(self, cbo: str):
        self.__cbo = cbo
