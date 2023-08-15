#! comentario Innecesario. (Misael G.)(37)
#! https://refactoring.guru/smells/comments
"""
Modulo donde se crea la Clase Monstruo junto
a sus atributos y sus metodos
"""


class Monstruo():
    #! comentario Innecesario. (Misael G.)(38)
    #! https://refactoring.guru/smells/comments
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
        #! comentario Innecesario. (Misael G.)(39)
        #! https://refactoring.guru/smells/comments
        """
        metodo morir
        """

        self.vivo = False
        print("Monstruo "+self.type_monstruo+" muerto")

    def dropea(self):
        #! utiliza pass para evitar errores. (Misael G.)(40)
        #! https://www.programiz.com/python-programming/pass-statement

        #! comentario Innecesario. (Misael G.)(41)
        #! https://refactoring.guru/smells/comments
        """
        Todavia no coloca  nada en este metodo
        """

    def estadisticas(self):
        #! comentario Innecesario. (Misael G.)(42)
        #! https://refactoring.guru/smells/comments
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
