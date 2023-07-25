from Monstruo import Monstruo 
class Creeper(Monstruo):
    

    def __init__(self):
        self.typeMonstruo = "Creeper"
        self.vida = 10
        self.daño = 5
        self.level = 5
        self.experiencia = 30
        self.vivo = True

    def Explota(self):
        print("hace 10 de daño")