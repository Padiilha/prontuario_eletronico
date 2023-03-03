from dao.abstract_dao import AbstractDAO
from model.cidadao import Cidadao


class CidadaoDao(AbstractDAO):
    def __init__(self):
        super().__init__('cidadaos.pkl')

    def add(self, key: int, obj: Cidadao):
        if obj is not None \
                and isinstance(obj, Cidadao) \
                and isinstance(key, int):
            super().add(key, obj)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
