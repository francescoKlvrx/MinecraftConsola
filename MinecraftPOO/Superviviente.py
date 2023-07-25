class Superviviente():

    def __init__(self):
        self.vida = 10
        self.level = 5
        self.movimiento = 1
        self.daño = 8
        self.experiencia = 30
        self.vivo = True


    def Moverse(self):
        if self.movimiento > 0:
            self.movimiento -1
            print("El superviviente se ha movido. movimientos restantes :",self.movimiento) 

    def Morir(self):        
        self.vivo = False
        print("Superviviente muerto")

    def Defenderse(self):
        pass

    def MostrarDatosJugador(self):

        print("Vida :",self.vida," daño :",self.daño," level :",self.level,"Exp :",self.experiencia)
        print("Cantidad de Movimientos : ",self.movimiento)
        print("Personaje vivo? :",self.vivo)

