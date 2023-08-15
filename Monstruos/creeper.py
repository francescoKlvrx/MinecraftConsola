#! comentario Innecesario. (Misael G.)(1)
#! https://refactoring.guru/smells/comments
"""
Modulo Donde se crea la clase hija de Monstruo
"""
from monstruo import Monstruo


class Creeper(Monstruo):
    #! comentario Innecesario. (Misael G.)(2)
    #! https://refactoring.guru/smells/comments
    """
    Clase donde se define los metodos del la clase hija
    Creeper.
    """

    def __init__(self):
        super().__init__()
        self.type_monstruo = "Creeper"
        self.vida = 10
        self.danio = 5
        self.level = 5
        self.experiencia = 30
        self.vivo = True

    def explota(self):
        """
        Este metodo es especial de Creeper
        """
        #! creo que sería mejor hacer que el print sea el valor de una variale,
        #! en este caso, el doble de self.danio. (Misael G.)(3)
        print("hace 10 de daño")
