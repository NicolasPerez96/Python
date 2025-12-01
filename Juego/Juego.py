from Heroe import campeon, guerrero, mago, picaro

from Enemigo import enemigoGenerico, goblin, lobo, troll

import random

print("""Bienvenidos a Terminal RPG
      -----------------------------
      
      Por favor seleccione su campeon""")


def darNombre():
    nombre = input("Introduzca el nombre de su campeon: ")
    return nombre

nuevo_campeon = input("""
                      1- Guerrero
                      2- Mago
                      3- Picaro 
                      Eleccion: """)

if nuevo_campeon == "1":
    nuevo_nombre = darNombre()
    jugador = guerrero(nuevo_nombre)
elif nuevo_campeon == "2":
    nuevo_nombre = darNombre()
    jugador = mago(nuevo_nombre)
elif nuevo_campeon == "3":
    nuevo_nombre = darNombre()
    jugador = picaro(nuevo_nombre)
else:
    print("No se selecciono ningun campeon.")
    

print(f"""Su campeon se llama {jugador.nombre} y tiene las estadisticas:
      vida: {jugador.vida_actual}
      fuerza: {jugador.fuerza}
      agilidad: {jugador.agilidad}
      velocidad: {jugador.velocidad}
      inteligencia: {jugador.inteligencia}
      -----------------------------------
      
      Suerte con su aventura.""")
    
def enemigoRandom():    
    enemigos = [goblin, lobo, troll]

    enemigo = random.choice(enemigos)
    return enemigo


def iniciarCombate(jugador, enemigo):
    dañoJugador = jugador.atacar()
    dañoEnemigo = enemigo.atacar()
    
    vidaEnemigo = enemigo.vida_actual
    vidaJugador = jugador.vida_actual
    
    while vidaJugador > 0 and vidaEnemigo > 0:
         vidaEnemigo -= dañoJugador
         vidaJugador -= dañoEnemigo
         break