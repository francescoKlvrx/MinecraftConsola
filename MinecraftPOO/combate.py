"""
    Modulo combate: en este modulo llamo a las distintas
    Clases para que simulen una pelea dentro de los metodos
    de esta clase.

"""

from Monstruos.zombie import Zombie
from Monstruos.creeper import Creeper
from Monstruos.esqueleto import Esqueleto
from superviviente import Superviviente


class Combate():
    """
    En esta Clase se da la pelea entre los monstruos y steve
    entre otras funcionalidades.
    """
    def __init__(self):

        self.__objetocreeper = Creeper()
        self.__objetozombie = Zombie()
        self.__objetoesqueleto = Esqueleto()
        self.__objetosuperviviente = Superviviente()

    def steve_ataca(self, monstruo):
        """
        Este metodo recibe como parametro el monstruo que steve
        va a atacar.
        """

        if monstruo == "Creeper":

            # En este if se toma en cuenta que steve este a dos metros
            # o menos del monstruo
            if self.__objetosuperviviente.distancia <= 2.0:

                self.__objetosuperviviente.mostrar_datos_jugador()
                self.__objetocreeper.estadisticas()

                print("\nSteve ataca a Creeper!!")
                self.__objetocreeper.vida -= self.__objetosuperviviente.danio
                # Cada vez que Steve le pegue al monstruo se le empujara
                # 0.5 metros hacia atras
                self.__objetosuperviviente.distancia += 0.5

                if self.__objetocreeper.vida <= 0:

                    self.__objetocreeper.morir()
                    self.__objetocreeper.dropea()

                    # Al morir el Monstruo se le reinicia
                    # la distancia al siguiente
                    self.__objetosuperviviente.distancia = 4

                else:
                    print("\nNUEVOS STATS DE CREEPER...")
                    self.__objetocreeper.estadisticas()

            else:
                # De esta forma no salta el error al trabajar con enteros

                distancia = f"Necesitas aercarte mas para pegarle. \
                \nactual distancia {self.__objetosuperviviente.distancia}"

                print(distancia)

        elif monstruo == "Zombie":

            if self.__objetosuperviviente.distancia <= 2.0:

                self.__objetosuperviviente.mostrar_datos_jugador()
                self.__objetozombie.estadisticas()

                print("\nSteve ataca a Zombie!!")
                self.__objetozombie.vida -= self.__objetosuperviviente.danio
                self.__objetosuperviviente.distancia += 0.5

                if self.__objetozombie.vida <= 0:

                    self.__objetozombie.morir()
                    self.__objetozombie.dropea()

                    self.__objetosuperviviente.distancia = 4

                else:
                    print("\nNUEVOS STATS DE ZOMBIE...")
                    self.__objetozombie.estadisticas()

            else:

                distancia = f"Necesitas aercarte mas para pegarle. \
                \nactual distancia {self.__objetosuperviviente.distancia}"

                print(distancia)

        elif monstruo == "Esqueleto":

            if self.__objetosuperviviente.distancia <= 2.0:

                self.__objetosuperviviente.mostrar_datos_jugador()
                self.__objetoesqueleto.estadisticas()

                print("\nSteve ataca a Esqueleto!!")
                self.__objetoesqueleto.vida -= self.__objetosuperviviente.danio
                self.__objetosuperviviente.distancia += 0.5

                if self.__objetoesqueleto.vida <= 0:

                    self.__objetoesqueleto.morir()
                    self.__objetoesqueleto.dropea()

                    self.__objetosuperviviente.distancia = 4

                else:
                    print("\nNUEVOS STATS DE ESQUELETO...")
                    self.__objetoesqueleto.estadisticas()

            else:

                distancia = f"Necesitas aercarte mas para pegarle. \
                \nactual distancia {self.__objetosuperviviente.distancia}"

                print(distancia)

        else:
            print("FALLA EN DEF STEVEATACA EN CLASE COMBATE")

    def monstruo_ataca(self, monstruo):
        """
        Este metodo al contrario que el anterior recibe como parametro
        el monstruo que esta atacando
        """

        if monstruo == "Creeper":

            # A diferencia de Steve el monstruo tiene que estar a
            # 1.5 metros para golpear a Steve
            if self.__objetosuperviviente.distancia <= 1.5:

                print("\nCreeper Golpeo a Steve!!")
                self.__objetosuperviviente.vida -= self.__objetocreeper.danio

                print("\nNUEVOS STATS DE STEVE...")
                self.__objetosuperviviente.mostrar_datos_jugador()

            else:
                # Comprueba que el monstruo este vivo para mostrar el print
                if self.__objetocreeper.vivo:

                    distancia = f"Ten Cuidado la distancia entre tu y el \
                    \nmonstruo es de :\
                    \n{self.__objetosuperviviente.distancia} metros"

                    print(distancia)

        elif monstruo == "Zombie":

            if self.__objetosuperviviente.distancia <= 1.5:

                print("\nZombie ataca a Steve!!")
                self.__objetosuperviviente.vida -= self.__objetozombie.danio

                print("NUEVOS STATS DE STEVE...")
                self.__objetosuperviviente.mostrar_datos_jugador()

            else:
                if self.__objetozombie.vivo:

                    distancia = f"Ten Cuidado la distancia entre tu y el \
                    \nmonstruo es de :\
                    \n{self.__objetosuperviviente.distancia} metros"

                    print(distancia)

        elif monstruo == "Esqueleto":

            if self.__objetosuperviviente.distancia <= 1.5:

                print("\nEqueleto ataca a Steve!!")
                self.__objetosuperviviente.vida -= self.__objetoesqueleto.danio

                print("NUEVOS STATS DE ESQUELETO...")
                self.__objetosuperviviente.mostrar_datos_jugador()

            else:
                if self.__objetoesqueleto.vivo:

                    distancia = f"Ten Cuidado la distancia entre tu y el \
                    \nmonstruo es de :\
                    \n{self.__objetosuperviviente.distancia} metros"

                    print(distancia)

        else:
            print("FALLA EN DEF MONSTRUOATACA EN CLASE COMBATE")

    def mostrar_estadisticas(self):
        """
        Este metodo muestra las estadisticas del jugador
        """

        self.__objetosuperviviente.mostrar_datos_jugador()

    def monstruo_se_acerca(self):
        """
        Este metodo acerca al monstruo al jugador
        """

        self.__objetosuperviviente.distancia -= 1.0

        aviso = f"\nEl monstruo está a {self.__objetosuperviviente.distancia}\
        \nmetros de Steve!!"

        print(aviso)

    def steve_se_acerca(self):
        """
        Este metodo acerca al jugador al monstruo
        """

        self.__objetosuperviviente.distancia -= 1.0

        aviso = f"\nSteve Se está acercando,\
        \n{self.__objetosuperviviente.distancia} metros de distancia"

        print(aviso)

    def steve_se_aleja(self):
        """
        Este metodo aleja al jugador del monstruo
        """

        self.__objetosuperviviente.distancia += 1.0

        aviso = f"\nSteve Se está alejando,\
        \n{self.__objetosuperviviente.distancia} metros de distancia"

        print(aviso)

    def steve_se_cubre(self, monstruo):
        """
        Este metodo cubre al jugador del monstruo
        """

        if monstruo == "Creeper":
            # Verifica que el monstruo este a distancia de golpe
            if self.__objetosuperviviente.distancia <= 1.5:

                self.__objetosuperviviente.defenderse_de_creeper()
            else:

                lejos = f"El monstruo esta muy lejos para golpearte.\
                \ndistancia {self.__objetosuperviviente.distancia} metros"

                print(lejos)

        elif monstruo == "Zombie":
            if self.__objetosuperviviente.distancia <= 1.5:

                self.__objetosuperviviente.defenderse_de_zombie()
            else:

                lejos = f"El monstruo esta muy lejos para golpearte.\
                \ndistancia {self.__objetosuperviviente.distancia} metros"

                print(lejos)

        elif monstruo == "Esqueleto":
            if self.__objetosuperviviente.distancia <= 1.5:

                self.__objetosuperviviente.defenderse_de_esqueleto()
            else:

                lejos = f"El monstruo esta muy lejos para golpearte.\
                \ndistancia {self.__objetosuperviviente.distancia} metros"

                print(lejos)

    def montruo_vivo(self, monstruo):
        """
        Este metodo verifica si el monstruo esta vivo
        """

        if monstruo == "Creeper":

            if not self.__objetocreeper.vivo:
                return False
            else:
                return True

        elif monstruo == "Zombie":

            if not self.__objetozombie.vivo:
                return False
            else:
                return True

        elif monstruo == "Esqueleto":

            if not self.__objetoesqueleto.vivo:
                return False
            else:
                return True

    def restaurar_stats(self, monstruo):
        """
        Este metodo restaura los stats del monstruo que le
        ingrese por parametro, verificando a la vez que este
        se encuentre vivo
        """

        if monstruo == "Creeper" and not self.__objetocreeper.vivo:

            self.__objetocreeper.vivo = True
            self.__objetocreeper.vida = 10

        elif monstruo == "Zombie" and not self.__objetozombie.vivo:

            self.__objetozombie.vivo = True
            self.__objetozombie.vida = 10

        elif monstruo == "Esqueleto" and not self.__objetoesqueleto.vivo:

            self.__objetoesqueleto.vivo = True
            self.__objetoesqueleto.vida = 10

    def mostrar_inventario(self):
        """
        Este metodo muestra el inventario del jugador
        """
        self.__objetosuperviviente.mostrar_inventario()


# fin clase combate
