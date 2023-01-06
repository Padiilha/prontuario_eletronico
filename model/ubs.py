

class Ubs:
    def __init__(self, seq_ubs: int, cnes: str, nome: str, bairro: str):
        self.__seq_ubs = seq_ubs
        self.__cnes = cnes
        self.__nome = nome
        self.__bairro = bairro

    @property
    def cnes(self) -> str:
        return self.__cnes

    @cnes.setter
    def cnes(self, cnes: str):
        self.__cnes = cnes

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def bairro(self) -> str:
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro: str):
        self.__bairro = bairro
