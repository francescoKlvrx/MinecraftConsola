from Monstruos import Zombie
from Monstruos import Creeper
from Monstruos import Esqueleto
from Superviviente import Superviviente
class Combate():
    

    def SteveAtaca(self, monstruo):
        objetoCreeper = Creeper.Creeper()
        ObjetoZombie = Zombie.Zombie()
        ObjetoEsqueleto = Esqueleto.Esqueleto()
        objetoSuperviviente = Superviviente()
        
        if monstruo == "Creeper":
            objetoSuperviviente.MostrarDatosJugador()
            objetoCreeper.Estadisticas()
            print("\n\n------------Steve ataca a Creeper-------------")
            objetoCreeper.vida = objetoCreeper.vida - objetoSuperviviente.daño
            print("NUEVOS STATS DE CREEPER")
            objetoCreeper.Estadisticas()           

        elif monstruo == "Zombie":
            objetoSuperviviente.MostrarDatosJugador()
            ObjetoZombie.Estadisticas()
            print("\n\n------------Steve ataca a Zombie-------------")
            objetoCreeper.vida = objetoCreeper.vida - objetoSuperviviente.daño
            print("NUEVOS STATS DE ZOMBIE")
            ObjetoZombie.Estadisticas()

        elif monstruo == "Esqueleto":
            objetoSuperviviente.MostrarDatosJugador()
            ObjetoEsqueleto.Estadisticas()
            print("\n\n------------Steve ataca a Esqueleto-------------")
            objetoCreeper.vida = objetoCreeper.vida - objetoSuperviviente.daño
            print("NUEVOS STATS DE ESQUELETO")
            ObjetoEsqueleto.Estadisticas()
        else:
            print("FALLA EN DEF DE ATAQUE EN CLASE COMBATE")

    def MonstruoAtaca(self,monstruo):
        objetoCreeper = Creeper.Creeper()
        ObjetoZombie = Zombie.Zombie()
        ObjetoEsqueleto = Esqueleto.Esqueleto()
        objetoSuperviviente = Superviviente()       

        if monstruo == "Creeper":
            objetoSuperviviente.MostrarDatosJugador()
            objetoCreeper.Estadisticas()
            print("\n\n------------Creeper ataca a Steve-------------")
            objetoSuperviviente.vida = objetoSuperviviente.vida - objetoCreeper.daño
            print("NUEVOS STATS DE CREEPER")
            objetoSuperviviente.MostrarDatosJugador()
            

        elif monstruo == "Zombie":
            objetoSuperviviente.MostrarDatosJugador()
            ObjetoZombie.Estadisticas()
            print("\n\n------------Zombie ataca a Steve-------------")
            objetoSuperviviente.vida = objetoSuperviviente.vida - ObjetoZombie.daño
            print("NUEVOS STATS DE ZOMBIE")
            objetoSuperviviente.MostrarDatosJugador()

        elif monstruo == "Esqueleto":
            objetoSuperviviente.MostrarDatosJugador()
            ObjetoEsqueleto.Estadisticas()
            print("\n\n------------Equeleto ataca a Steve-------------")
            objetoSuperviviente.vida = objetoSuperviviente.vida - ObjetoEsqueleto.daño
            print("NUEVOS STATS DE ESQUELETO")
            objetoSuperviviente.MostrarDatosJugador()

        else:
            print("FALLA EN DEF DE ATAQUE EN CLASE COMBATE")
    