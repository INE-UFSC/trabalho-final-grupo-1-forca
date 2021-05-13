from personagem import Personagem
from laser import Laser
WIDTH, HEIGHT = 600, 600

def Atirar(personagem: Personagem):
    laser = Laser(int(personagem.x + (personagem.personagem_img.get_width()/2) - (personagem.laser_img.get_width()/2)),
                  int(personagem.y-10), HEIGHT, personagem.laser_img)
    return laser
