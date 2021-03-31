from Objeto import Objeto

class Meteoro(Objeto):
    @abstractmethod
    def __init__(self, posicao_x: int, posicao_y: int, tamanho_x: int, tamanho_y: int, velocidade: int, vida: int, ativo: int, impacto: int):
        super().__init__(posicao_x, posicao_y, tamanho_x, tamanho_y, velocidade, vida, ativo)
        self.__impacto = impacto  


    #############
    #getters e setters

    #impacto
    @impacto
    def impacto(self):
        return self.__impacto

    @impacto.setter
    def impacto(self, impacto: int):
        self.__impacto = impacto

    ##############
    #métodos
    def desenhar(self, posicao_x, posicao_y):
        pass

    def mover(self):
        pass
    

