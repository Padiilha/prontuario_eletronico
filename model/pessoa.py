from abc import ABC

from model.consulta import Consulta


class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, cns: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__cns = [cns]
        self.__historico_consulta = list()

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def cns(self) -> list:
        return self.__cns

    @cns.setter
    def cns(self, cns: str):
        self.__cns.append(cns)

    @property
    def historico_consulta(self) -> list:
        return self.__historico_consulta

    def add_consulta(self, consulta: Consulta):
        self.__historico_consulta.append(consulta)
