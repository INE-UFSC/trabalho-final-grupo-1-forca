from abc import ABC, abstractmethod

class Objeto(ABC):

    def __init__(self):
        self.__posicao_x = 0
        self.__posicao_y = 0
        self.__tamanho_x = 0
        self.__tamanho_y = 0
        self.__velocidade = 0
        self.__vida = 0

    ##############
    #getters e setters

    #posicao x
    @property
    def posicao_x(self):
        return self.__posicao_x

    @posicao_x.setter
    def posicao_x(self, x: int):
        self.__posicao_x = x

    #posicao y
    @property
    def posicao_y(self):
        return self.__posicao_y

    @posicao_y.setter
    def posicao_y(self, y: int):
        self.__posicao_y = y

    #tamanho x
    @property
    def tamanho_x(self):
        return self.__tamanho_x

    @tamanho_x.setter
    def tamanho_x(self, x: int):
        self.__tamanho_x = x

    #tamanho y
    @property
    def tamanho_y(self):
        return self.__tamanho_y

    @tamanho_y.setter
    def tamanho_y(self, y: int):
        self.__tamanho_y = y

    #velocidade
    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade: int):
        self.__velocidade = velocidade

    #vida
    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida: int):
        self.__vida = vida

    ##################
    #métodos abstratos
    @abstractmethod
    def desenhar(self, surface):
        pass

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def colisao(self):
        pass
