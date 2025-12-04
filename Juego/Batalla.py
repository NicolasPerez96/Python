from Heroe import campeon, guerrero, mago, picaro

from Enemigo import enemigoGenerico, goblin, lobo, troll

import random

def enemigoRandom():    
        enemigos = [goblin, lobo, troll]

        enemigo_random = random.choice(enemigos)
        
        enemigo_seleccionado = enemigo_random()
        return enemigo_seleccionado

def iniciarCombate(jugador, enemigo):     
    
    while jugador.vida_actual > 0 and enemigo.vida_actual > 0:
         opcion = input(f"""
                        1- Atacar
                        2- Intentar correr
                        Op: """)
         if opcion == "1":             
            dañoJugador = jugador.atacar()
            enemigo.recibirDaño(dañoJugador)
            if enemigo.vida_actual <= 0:
                print(f"{enemigo.nombre} ha sido derrotado.")
                if isinstance(enemigo, goblin):
                    print(f"{jugador.nombre} ha ganado 15 de experiencia")
                    jugador.experiencia += 100
                elif isinstance(enemigo, lobo):
                    print(f"{jugador.nombre} ha ganado 25 de experiencia")
                    jugador.experiencia += 100                    
                elif isinstance(enemigo, troll):
                    print(f"{jugador.nombre} ha ganado 50 de experiencia")
                    jugador.experiencia += 70
                
                if jugador.experiencia_subir_nivel <= jugador.experiencia:
                    jugador.subirNivel()
                break
            dañoEnemigo = enemigo.atacar()
            jugador.recibirDaño(dañoEnemigo)
            if not jugador.estaVivo():
                print(f"""
                    {jugador.nombre} ha sido derrotado.
                    Fin de la aventura.""")
                break
            elif opcion == "2":
                break
            else:
                print("Opcion incorrecta.")
    
         
def menuCombate(jugador):
    enemigo = enemigoRandom()
    print (f"Te has topado con {enemigo.nombre}")
    
    if jugador.estaVivo() :        
        opcion = input("""
                    ---------------------
                    1- Pelear
                    2- Huir
                    Op: """)
        if opcion == "1":
            iniciarCombate(jugador, enemigo)
        else:
            return
         
        