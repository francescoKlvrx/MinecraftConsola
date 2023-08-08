"""
Modulo donde se crea la Clase Monstruo junto
a sus atributos y sus metodos
"""


class Monstruo():
    """
    Clase Monstruo
    """

    def __init__(self):
        self.type_monstruo = ""
        self.vida = 0
        self.level = 0
        self.danio = 0
        self.vivo = True
        self.experiencia = 0

    def morir(self):
        """
        metodo morir
        """

        self.vivo = False
        print("Monstruo "+self.type_monstruo+" muerto")

    def dropea(self):
        """
        Todavia no coloca  nada en este metodo
        """

    def estadisticas(self):
        """
        metodo donde se muestran las estadisticas del monstruo
        """

        stats_vida = f"vida total: {self.vida}"
        corazones = "♡ " * self.vida
        stats_danio = f"daño total: {self.danio}"
        level = f"nivel de monstruo: {self.level}"

        print("\n-------------------Datos de Monstruo----------------------")
        print("Estadisticas de "+self.type_monstruo+": ")
        print(stats_vida)
        print(corazones)
        print(stats_danio)
        print(level)
