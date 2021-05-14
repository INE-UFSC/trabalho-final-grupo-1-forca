from personagem import Personagem
from laser import Laser


def Atirar(personagem: Personagem, height: int, width: int):
    laser = Laser(int(personagem.x + (personagem.personagem_img.get_width()/2) - (personagem.laser_img.get_width()/2)),
                  int(personagem.y-10), height, width, personagem.laser_img)
    return laser