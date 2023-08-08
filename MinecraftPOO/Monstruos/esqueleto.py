"""
Modulo esqueleto
"""

from monstruo import Monstruo


class Esqueleto(Monstruo):
    """
    Clase esqueleto
    """

    def __init__(self):
        super().__init__()
        self.type_monstruo = "Esqueleto"
        self.vida = 12
        self.danio = 6
        self.level = 5
        self.experiencia = 30
        self.vivo = True
