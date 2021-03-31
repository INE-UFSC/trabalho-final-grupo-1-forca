from Objeto import Objeto

class Jogador(Objeto):
    @abstractmethod
    def __init__(self, posicao_x: int, posicao_y: int, tamanho_x: int, tamanho_y: int, velocidade: int, vida: int, ativo: int, pontuacao: int, forca: float, escudo: bool):
        super().__init__(posicao_x, posicao_y, tamanho_x, tamanho_y, velocidade, vida, ativo)
        self.__pontuacao = pontuacao
        self.__forca = forca
        self.__escudo = escudo        

    #############
    #getters e setters

    #pontuacao
    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, pontuacao: int):
        self.__pontuacao = pontuacao

    #forca
    @property
    def forca(self):
        return self.__forca

    @forca.setter
    def forca(self, forca: float):
        self.__forca = forca

    #escudo
    @property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def escudo(self, escudo: bool):
        self.__escudo = escudo

    #############
    #métodos
    def atirar(self):
        pass

    def desenhar(self, posicao_x, posicao_y):
        pass

    def mover(self):
        pass


