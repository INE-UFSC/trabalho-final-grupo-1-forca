from abc import ABC, abstractmethod


class Objeto(ABC):
    @abstractmethod
    def __init__(self, x: int, y: int, height: int, width: int):
        self.__x = x
        self.__y = y
        self.__height = height
        self.__width = width
        self.__objeto_img = None
        self.__mascara = None
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width
     
    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    def desenhar(self, window):
        window.blit(self.objeto_img, (self.x, self.y))
    
    def colisao(self, objeto, lista):
        offset_x = int(objeto.x - self.x)
        offset_y = int(objeto.y - self.y)
        colisao = self.mascara.overlap(objeto.mascara, (offset_x, offset_y)) != None

        if colisao:
            try:
                lista.remove(self)
            except ValueError:
                print("ValueError")
                pass  
        return colisao

    def fora_da_tela(self):
        return ((self.y > self.height) or (self.x > self.width))

    def movimentar(self, velocidade, lista):
        self.y += velocidade
        if self.fora_da_tela():
            try:
                lista.remove(self)
            except ValueError:
                print("ValueError")
                pass  
            
    def get_width(self):
        return self.objeto_img.get_width()
    
    def get_height(self):
        return self.objeto_img.get_height()

    @property
    @abstractmethod
    def objeto_img(self):
        pass

    @property
    @abstractmethod
    def mascara(self):
        pass