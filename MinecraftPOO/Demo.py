from Combate import Combate

print("EMPIEZA EL JUEGO")
#En este caso solo esta desarrollada la funcion de atacar 

#instancia de la clase combate
objetoCombate = Combate()

#Ahora pondremos a pelear a steve con algunos monstruos

objetoCombate.SteveAtaca("Creeper")
objetoCombate.SteveAtaca("Esqueleto")

#ahora un monstruo le respondera a steve

objetoCombate.MonstruoAtaca("Zombie")