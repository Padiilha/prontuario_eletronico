from dao.abstract_dao import AbstractDAO
from model.profissional import Profissional


class ProfissionalDao(AbstractDAO):
    def __init__(self):
        super().__init__('profissionais.pkl')

    def add(self, key: int, obj: Profissional):
        if obj is not None \
                and isinstance(obj, Profissional) \
                and isinstance(key, int):
            super().add(key, obj)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
