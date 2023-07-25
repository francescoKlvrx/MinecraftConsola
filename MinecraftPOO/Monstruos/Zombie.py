from Monstruo import Monstruo 
class Zombie(Monstruo):

    def __init__(self):
        self.typeMonstruo = "Zombie"
        self.vida = 10
        self.daño = 7
        self.level = 5
        self.experiencia = 30
        self.vivo = True

    def TieneUnArma(self):

        print("Tengo un arma")