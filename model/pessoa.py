from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, cns: str):
        self.__seq_pessoa = int
        self.__nome = nome
        self.__cpf = cpf
        self.__cns = [cns]

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
    def cns(self, cns: str):
        self.__cns = cns

    @cns.setter
    def cns(self) -> str:
        return self.__cns
