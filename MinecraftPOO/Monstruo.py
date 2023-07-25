
class Monstruo():

    def __init__(self):
        self.typeMonstruo = ""
        self.vida = 0
        self.level = 0
        self.daño = 0
        self.vivo = True
        self.experiencia = 0

    def Morir(self):

        self.vivo = False
        print("Monstruo ",self.typeMonstruo," muerto")

    def Dropea(self):
        pass

    def Estadisticas(self):
        print("Estadisticas de ",self.typeMonstruo,": ")
        print("vida: ",self.vida,"\ndaño: ",self.daño,"\nlevel :",self.level)