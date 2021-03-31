from Objeto import Objeto

class Inimigo(Objeto):
    @abstractmethod
    def __init__(self, posicao_x: int, posicao_y: int, tamanho_x: int, tamanho_y: int, velocidade: int, vida: int, ativo: int, forca: float):
        super().__init__(posicao_x, posicao_y, tamanho_x, tamanho_y, velocidade, vida, ativo)
        self.__forca = forca  

    #############
    #getters e setters

    #forca
    @forca
    def forca(self):
        return self.__forca

    @forca.setter
    def forca(self, forca: float):
        self.__forca = forca

    ##############
    #métodos
    def atirar(self):
        pass

    def desenhar(self, posicao_x, posicao_y):
        pass

    def mover(self):
        pass
    

