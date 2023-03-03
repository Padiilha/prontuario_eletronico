from model.cidadao import Cidadao
from model.profissional import Profissional
from model.ubs import Ubs


class Consulta:
    def __init__(self, seq_consulta: int, profissional: Profissional, cidadao: Profissional, ubs: Ubs, data_consulta: str):
        self.__seq_consulta = seq_consulta
        self.__profissional = profissional
        self.__cidadao = cidadao
        self.__ubs = ubs
        self.__data_consulta = data_consulta
        self.__soap = list()

    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @property
    def cidadao(self) -> Profissional:
        return self.__cidadao

    @property
    def ubs(self) -> Ubs:
        return self.__ubs

    @property
    def data_consulta(self) -> str:
        return self.__data_consulta

    def subjetivo(self, subjetivo: str):
        self.__soap.append(subjetivo)

    def objetivo(self, objetivo: str):
        self.__soap.append(objetivo)

    def avaliacao(self, avaliacao: str):
        self.__soap.append(avaliacao)

    def plano(self, plano: str):
        self.__soap.append(plano)
