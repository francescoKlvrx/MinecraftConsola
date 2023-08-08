"""
Modulo Donde se crea la clase hija de Monstruo
"""
from monstruo import Monstruo


class Creeper(Monstruo):
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
        print("hace 10 de daño")
