#! comentario Innecesario. (Misael G.)(6)
#! https://refactoring.guru/smells/comments
"""
Modulo donde se crea la clase Zombie
"""

from monstruo import Monstruo


class Zombie(Monstruo):
    #! comentario Innecesario. (Misael G.)(7)
    #! https://refactoring.guru/smells/comments
    """
    Clase Zombie
    """

    def __init__(self):
        super().__init__()
        self.type_monstruo = "Zombie"
        self.vida = 10
        self.danio = 3
        self.level = 5
        self.experiencia = 30
        self.vivo = True

    def tiene_un_arma(self):
        #! no comprendo lo de random, es un place holder? .(Misael G.)(8)
        """
        Metodo random
        """
        print("Tengo un arma")
