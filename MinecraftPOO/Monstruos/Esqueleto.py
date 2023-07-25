from Monstruo import Monstruo 
class Esqueleto(Monstruo):

    def __init__(self):
        self.typeMonstruo = "Esqueleto"
        self.vida = 12
        self.daño = 10
        self.level = 5
        self.experiencia = 30
        self.vivo = True