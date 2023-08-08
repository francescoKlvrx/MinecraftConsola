"""
Francesco Montalva - Kloverx
06/08/2023

Codigo del juego de minicraft echo con POO

Modulo demo: Este modulo lo utilizo de clase main y llamo
a la clase combate para dar a acabo la pelea en un ciclo while
"""

import random
import time
import os
from combate import Combate

# Comienzo del juego
print("----------------------MINECRAFT----------------------")
print("Comenzar")
os.system('pause')
time.sleep(1)
os.system('cls')

# Esta funcion se encarga de entregar un numero aleatorio entre
# entre dos valores que le des
posicionX = random.randrange(-10001, 10001, 2)
posicionY = random.randrange(-10001, 10001, 2)

objetoCombate = Combate()

# Introduccionn al jugador
print("Eres un personaje Steve en el videojuego famoso de Minecraft.")
print("y acabas de respawnear en las siguientes coordenadas: ")
posiciones = f"X: {posicionX} Y: {posicionY}"

print(posiciones)

objetoCombate.mostrar_estadisticas()
os.system('pause')
time.sleep(1)
os.system('cls')

print("Apura!! un Monstruo viene Acercandose")
objetoCombate.monstruo_se_acerca()
os.system('pause')
time.sleep(1)
os.system('cls')

# Aca usamos igual una funcion random pero esta es de tipo "choice" lo que hace
# es darnos un string aleatorio dentro de los que le estamos otorgando
print("Veamos de que tipo es...")
Monstruo = random.choice([
    "Creeper",
    "Zombie",
    "Esqueleto"
])

print("Oh ya veo, es un "+Monstruo)
print("De Momento pasemos de el y vamos a por otro. Ahora si.")
print("Que comience el juego...")
os.system('pause')
time.sleep(1)
os.system('cls')

# Constantes para entrar y salir de los bucles
ACTIVADOR_PRINCIPAL = 0
ACTIVADOR_SUBMENU = 0

while ACTIVADOR_PRINCIPAL == 0:

    print("Nuevo Monstruo!")
    print("Veamos de que tipo es...")
    Monstruo1 = random.choice([
        "Creeper",
        "Zombie",
        "Esqueleto"
    ])
    print(Monstruo1)

    objetoCombate.restaurar_stats(Monstruo1)

    print("\nQue vas a hacer a continuación?")
    print("1.Pelear")
    print("2.Ver inventario")
    print("3.Salir del juego")
    VarElegidaMenuPrincipal = int(input())
    os.system('pause')
    time.sleep(1)
    os.system('cls')

    match VarElegidaMenuPrincipal:

        case 1:
            ACTIVADOR_SUBMENU = 1

        case 2:
            objetoCombate.mostrar_inventario()

        case 3:
            objetoCombate.mostrar_estadisticas()
            print("FIN DEL JUEGO")
            ACTIVADOR_PRINCIPAL = 1

    while ACTIVADOR_SUBMENU == 1:

        # Aca estoy comprobando que el monstruo este vivo para mostrar el print
        # De no estarlo lo deja continuar pero no muestra el print
        if objetoCombate.montruo_vivo(Monstruo1):
            print("Ahora estas peleando con un "+Monstruo1)
        else:
            pass

        print("\nQue vas a hacer a continuación?")
        print("1.Atacar")
        print("2.Acercarte Más")
        print("3.Alejarte")
        print("4.Cubrirte")
        print("5.Pelear Con otro Monstruo")
        VarElegidaSubMenu = int(input())
        os.system('pause')
        time.sleep(1)
        os.system('cls')

        match VarElegidaSubMenu:

            case 1:
                objetoCombate.steve_ataca(Monstruo1)
                objetoCombate.monstruo_ataca(Monstruo1)
                os.system('pause')
                time.sleep(1)
                os.system('cls')

            case 2:
                objetoCombate.steve_se_acerca()
                objetoCombate.monstruo_ataca(Monstruo1)
                os.system('pause')
                time.sleep(1)
                os.system('cls')

            case 3:
                objetoCombate.steve_se_aleja()
                objetoCombate.monstruo_ataca(Monstruo1)
                os.system('pause')
                time.sleep(1)
                os.system('cls')

            case 4:
                objetoCombate.monstruo_ataca(Monstruo1)
                objetoCombate.steve_se_cubre(Monstruo1)
                os.system('pause')
                time.sleep(1)
                os.system('cls')

            case 5:
                objetoCombate.steve_se_aleja()
                objetoCombate.steve_se_aleja()
                print("Buscando Otro Monstruo...")
                os.system('pause')
                time.sleep(1)
                os.system('cls')
                ACTIVADOR_SUB_MENU = 0
                ACTIVADOR_PRINCIPAL = 0
                break
