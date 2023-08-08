"""
Modulo donde se crea la clase Zombie
"""

from monstruo import Monstruo


class Zombie(Monstruo):
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
        """
        Metodo random
        """
        print("Tengo un arma")
