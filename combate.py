#! comentario Innecesario. (Misael G.)(9)
#! https://refactoring.guru/smells/comments
"""
    Modulo combate: en este modulo llamo a las distintas
    Clases para que simulen una pelea dentro de los metodos
    de esta clase.

"""
#! Creo que sería mejor unir todos los monstruos bajo la clase monstruo,
#! especialmente porque son implementaciones de la clase monstruo. (Misael G.)
#! (10)
from Monstruos.zombie import Zombie
from Monstruos.creeper import Creeper
from Monstruos.esqueleto import Esqueleto
from superviviente import Superviviente


class Combate():
    #! comentario Innecesario. (Misael G.)(11)
    #! https://refactoring.guru/smells/comments
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
        #! comentario Innecesario. (Misael G.)(12)
        #! https://refactoring.guru/smells/comments
        """
        Este metodo recibe como parametro el monstruo que steve
        va a atacar.
        """
        #! Usar Switch - case es mejor para la legibilidad del código, al igual
        #! que optimiza un poco el uso de memoria, aunque no es necesario,
        #! no sería malo aplicarlo. (Misael G.)(13)
        #! https://www.notion.so/aspirina180mg/Kloverx-Py-ff06214d4dba463eba5ea0101d9cc7f3?pvs=4#77ad694f3efc4d4cbf31b6783429f911
        if monstruo == "Creeper":

            #! comentario Innecesario. (Misael G.)(14)
            #! https://refactoring.guru/smells/comments
            # En este if se toma en cuenta que steve este a dos metros
            # o menos del monstruo
            if self.__objetosuperviviente.distancia <= 2.0:
                #! si recibe el objeto monstruo, que será de un tipo, no es
                #! necesario diferenciar las acciones para cada criatura,
                #! debería ser más facil llamar los datos de los monstruos, en
                #! especial porque son implementaciones de la clase monstruo.
                #! (Misael G.)(15)
                self.__objetosuperviviente.mostrar_datos_jugador()
                self.__objetocreeper.estadisticas()
                #! hacer un llamado de type_monstruo para conseguir el nombre
                #! del monstruo sin tener que utilizar un if else o un switch.
                #! (Misael G.)(16)
                print("\nSteve ataca a Creeper!!")
                self.__objetocreeper.vida -= self.__objetosuperviviente.danio
                #! podrías crear un método que se llame empuje, para facilitar
                #! la legibilidad del código. (Misael G.)(17)
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
                #! comentario Innecesario. (Misael G.)(18)
                #! https://refactoring.guru/smells/comments
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
        #! comentario Innecesario. (Misael G.)(19)
        #! https://refactoring.guru/smells/comments
        """
        Este metodo al contrario que el anterior recibe como parametro
        el monstruo que esta atacando
        """
        #! utilizar switch - case y llamado desde la clase.
        #! se repite mucho el mismo código con diferencias pequeñas.
        #! (Misael G.)(20)
        if monstruo == "Creeper":

            #! se podría asignar un nombre a la variable para que sea más
            #! legible, evitando el comentario (Misael G.)(21)
            #! https://refactoring.guru/smells/comments
            #! self.__objetosuperviviente.distancia = distancia_de_golpe
            #! if distancia_de_golpe <= 1.5:
            # A diferencia de Steve el monstruo tiene que estar a
            # 1.5 metros para golpear a Steve
            if self.__objetosuperviviente.distancia <= 1.5:

                print("\nCreeper Golpeo a Steve!!")
                self.__objetosuperviviente.vida -= self.__objetocreeper.danio

                print("\nNUEVOS STATS DE STEVE...")
                self.__objetosuperviviente.mostrar_datos_jugador()

            else:
                #! comentario Innecesario. (Misael G.)(22)
                #! https://refactoring.guru/smells/comments
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

    #! El método es de 1 línea de código, es necesario?
    #! Creo que no ahorra líneas de código ni facilita la legibilidad.
    #! (Misael G.)(23)
    def mostrar_estadisticas(self):
        #! comentario Innecesario. (Misael G.)(24)
        #! https://refactoring.guru/smells/comments
        """
        Este metodo muestra las estadisticas del jugador
        """

        self.__objetosuperviviente.mostrar_datos_jugador()

    def monstruo_se_acerca(self):
        #! comentario Innecesario. (Misael G.)(25)
        #! https://refactoring.guru/smells/comments
        """
        Este metodo acerca al monstruo al jugador
        """

        self.__objetosuperviviente.distancia -= 1.0

        aviso = f"\nEl monstruo está a {self.__objetosuperviviente.distancia}\
        \nmetros de Steve!!"

        print(aviso)

    #! Se podría crear un método steve_se_mueve y que decida el mensaje
    #! según si el valor de movimiento es mayor o menor a 0, de este modo se
    #! pueden juntar ambos métodos de movimiento en 1. (Misael G.)(26)
    #!
    def steve_se_acerca(self):
        #! comentario Innecesario. (Misael G.)(27)
        #! https://refactoring.guru/smells/comments
        """
        Este metodo acerca al jugador al monstruo
        """

        self.__objetosuperviviente.distancia -= 1.0

        aviso = f"\nSteve Se está acercando,\
        \n{self.__objetosuperviviente.distancia} metros de distancia"

        print(aviso)

    def steve_se_aleja(self):
        #! comentario Innecesario. (Misael G.)(28)
        #! https://refactoring.guru/smells/comments
        """
        Este metodo aleja al jugador del monstruo
        """

        self.__objetosuperviviente.distancia += 1.0

        aviso = f"\nSteve Se está alejando,\
        \n{self.__objetosuperviviente.distancia} metros de distancia"

        print(aviso)

    def steve_se_cubre(self, monstruo):
        #! comentario Innecesario. (Misael G.)(29)
        #! https://refactoring.guru/smells/comments
        """
        Este metodo cubre al jugador del monstruo
        """
        #! aplicar switch case y llamado desde la clase. (Misael G.)(30)
        #! https://www.notion.so/aspirina180mg/Kloverx-Py-ff06214d4dba463eba5ea0101d9cc7f3?pvs=4#2b4e63612f9546df95108399cffc61c7
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
        #! comentario Innecesario. (Misael G.)(31)
        #! https://refactoring.guru/smells/comments
        """
        Este metodo verifica si el monstruo esta vivo
        """
        #! aplicar switch case y llamado desde la clase. (Misael G.)(32)
        #! https://www.notion.so/aspirina180mg/Kloverx-Py-ff06214d4dba463eba5ea0101d9cc7f3?pvs=4#2b4e63612f9546df95108399cffc61c7
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
        #! aplicar switch case y llamado desde la clase. (Misael G.)(33)
        #! https://www.notion.so/aspirina180mg/Kloverx-Py-ff06214d4dba463eba5ea0101d9cc7f3?pvs=4#2b4e63612f9546df95108399cffc61c7
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
        #! comentario Innecesario. (Misael G.)(34)
        #! https://refactoring.guru/smells/comments
        """
        Este metodo muestra el inventario del jugador
        """
        self.__objetosuperviviente.mostrar_inventario()

#! comentario Innecesario. (Misael G.)(35)
#! https://refactoring.guru/smells/comments
# fin clase combate
