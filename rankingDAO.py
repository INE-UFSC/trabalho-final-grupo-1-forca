from DAO import DAO


class RankingDAO(DAO):
    def __init__(self):
        super().__init__('ranking.pkl')
        self.id = len(self.get_all())

    def add(self, nome, pontuacao):   # chave é um id e o valor é uma tupla com nome e pontuação
        valor_ranking = (nome, pontuacao)
        super().add(self.id, valor_ranking)
        self.id += 1
        print(self.id)

    def get_all(self):
        return super().get_all()

    """
    def get(self, nome):
        return super().get(nome)

    def remove(self, nome):
        super().remove(nome)
    """