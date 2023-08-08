"""
En este modulo se crea la clase superviviente y se le otorga
sus atributos y metodos.
"""


class Superviviente():
    """
    Clase Superviviente
    atributos y metodos basicos.
    """
    def __init__(self):
        self.vida = 10
        self.level = 5
        self.distancia = 4.0
        self.danio = 8
        self.experiencia = 30
        self.inventario = ["Espada de Madera", "Pico de Madera", "Carne Cruda"]
        self.vivo = True

    def morir(self):
        """
        Metodo morir
        """
        self.vivo = False
        print("Superviviente muerto")

    def defenderse_de_creeper(self):
        """
        Metodo defenderse_de_creeper
        """
        # En estos metodos buscamos un escudo, de no encontrarlo
        # te manda un print
        for inven in self.inventario:
            if inven == "Escudo":
                print("Daño ocasionado 0!")
                self.vida += 5
            else:
                print("No tienes un escudo en tu inventario. Consigue")
                print("uno para poder cubrirte de los monstruos!!")

    def defenderse_de_zombie(self):
        """
        Metodo defenderse_de_zombie
        """
        for inven in self.inventario:
            if inven == "Escudo":
                print("Daño ocasionado 0!")
                self.vida += 3
            else:
                print("No tienes un escudo en tu inventario. Consigue")
                print("uno para poder cubrirte de los monstruos!!")

    def defenderse_de_esqueleto(self):
        """
        Metodo defenderse_de_esqueleto
        """
        for inven in self.inventario:
            if inven == "Escudo":
                print("Daño ocasionado 0!")
                self.vida += 6
            else:
                print("No tienes un escudo en tu inventario. ")
                print("Consigue uno para poder cubrirte de los monstruos!!")

    def mostrar_datos_jugador(self):
        """
        Metodo mostrar_datos_jugador
        """
        # Decici hacerlo de esta forma ya que me daba un error
        # en la syntaxis por que mis variables son de tipo "int"
        #  y no las podia concadenar en un print con "+"
        stats_vida = f"Estas son tus Estadisticas: \nVida Total: {self.vida}"
        corazones = "♡ " * self.vida
        stats_danio = f"daño total: {+self.danio}"
        stats_level = f"Nivel de Steve: {+self.level}"
        stats_exp = f"Experiencia total: {self.experiencia}"

        print("\n--------------------Datos de Jugador-----------------------")
        print(stats_vida)
        print(corazones)
        print(stats_danio)
        print(stats_level)
        print(stats_exp)

    def mostrar_inventario(self):
        """
        Metodo mostrar_inventario
        """
        for items in self.inventario:
            print("-"+items)
