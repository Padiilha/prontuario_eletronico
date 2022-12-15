from model.pessoa import Pessoa


class Cidadao(Pessoa):
    def __init__(self, nome: str, cpf: str, cns: str):
        super().__init__(nome, cpf, cns)
        self.__historico_consultas = None
