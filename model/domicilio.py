from model.cidadao import Cidadao


class Domicilio:
    def __init__(self, seq_domicilio: int, logradouro: str, num_logradouro: int, bairro: str, cidade: str):
        self.__seq_domicilio = seq_domicilio
        self.__logradouro = logradouro
        self.__num_logradouro = num_logradouro
        self.__bairro = bairro
        self.__cidade = cidade
        self.__moradores = list()

    @property
    def logradouro(self) -> str:
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro: str):
        self.__logradouro = logradouro

    @property
    def num_logradouro(self) -> int:
        return self.__num_logradouro

    @num_logradouro.setter
    def num_logradouro(self, num_logradouro: int):
        self.__num_logradouro = num_logradouro

    @property
    def bairro(self) -> str:
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro: str):
        self.__bairro = bairro

    @property
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    def add_morador(self, morador: Cidadao):
        pass

    def rmv_morador(self, morador: Cidadao):
        pass
