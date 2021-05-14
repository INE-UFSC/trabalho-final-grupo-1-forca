from DAO import DAO
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class RankingDAO(DAO):
    def __init__(self):
        super().__init__(BASE_DIR+'/ranking.pkl')
        self.id = len(self.get_all())

    def add(self, nome, pontuacao):   # chave é um id e o valor é uma tupla com nome e pontuação
        valor_ranking = (nome, pontuacao)
        super().add(self.id, valor_ranking)
        self.id += 1

    def get_all(self):
        return super().get_all()