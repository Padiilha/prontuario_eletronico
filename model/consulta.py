from model.cidadao import Cidadao
from model.profissional import Profissional
from model.ubs import Ubs


class Consulta:
    def __init__(self, seq_consulta: int, profissional: Profissional, cidadao: Cidadao, ubs: Ubs, data_consulta: str):
        self.__seq_consulta = seq_consulta
        self.__profissional = profissional
        self.__cidadao = cidadao
        self.__ubs = ubs
        self.__data_consulta = data_consulta
        self.__soap = list()
