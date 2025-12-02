from Heroe import campeon, guerrero, mago, picaro

from Enemigo import enemigoGenerico, goblin, lobo, troll

import random



def darNombre():
    nombre = input("Introduzca el nombre de su campeon: ")
    return nombre


def enemigoRandom():    
    enemigos = [goblin, lobo, troll]

    enemigo_random = random.choice(enemigos)
    
    enemigo_seleccionado = enemigo_random()
    return enemigo_seleccionado


def iniciarCombate(jugador, enemigo):     
    
    while jugador.vida_actual > 0 and enemigo.vida_actual > 0:
         dañoJugador = jugador.atacar()
         enemigo.recibirDaño(dañoJugador)
         if enemigo.vida_actual <= 0:
             print(f"{enemigo.nombre} ha sido derrotado.")
             break
         dañoEnemigo = enemigo.atacar()
         jugador.recibirDaño(dañoEnemigo)
         if not jugador.estaVivo():
             print(f"""
                   {jugador.nombre} ha sido derrotado.
                   Fin de la aventura.""")
             break
         

def nuevaAventura(): 
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
    return jugador



def menuCombate(jugador):
    enemigo = enemigoRandom()
    print (f"Te has topado con {enemigo.nombre}")
    
    if jugador.estaVivo() :        
        opcion = input("""
                    ---------------------
                    1- Atacar
                    2- Huir
                    Op: """)
        if opcion == "1":
            iniciarCombate(jugador, enemigo)
        else:
            return
#----------------------------------------------

def jugar(jugador):
    print("Elije una opcion: ")
    opcion = input("""
          1- Combatir
          2- Descansar
          3- Ver estadisticas
          4- Salir
          Op: """)
    if opcion == "1":
        menuCombate(jugador)
    elif opcion == "2":
        print(f"{jugador.nombre} descansa en la fogata.")
        print(f"{jugador.nombre} recupera 20 de vida")
        jugador.recuperarVida(20)
        return True
    elif opcion == "3":
        print(f"""Su campeon se llama {jugador.nombre} y tiene las estadisticas:
              vida: {jugador.vida_actual}
              fuerza: {jugador.fuerza}
              agilidad: {jugador.agilidad}
              velocidad: {jugador.velocidad}
              inteligencia: {jugador.inteligencia}""")
    elif opcion == "4":
        print("Seguro desea salir?")
        opcion2 = input("""
                        1- Si
                        2- No
                        Op: """)
        if opcion2 == "1":
            exit()
        elif opcion2 == "2":
            return True
    else:
        print("Opcion incorrecta.")
        return


def comenzarAventura():
    print("""Bienvenidos a Terminal RPG
      -----------------------------
      
      Por favor seleccione su campeon""")
    jugador = nuevaAventura()
    
    if jugador is None:
        print("Error al crear el campeón. Saliendo.")
        return
    
    print (f"¡{jugador.nombre}, comienza la aventura!")
    
    # Bucle Principal de la Aventura (Paso G)
    while jugador.estaVivo():
        continuar_juego = jugar(jugador)
        
        # Comprueba si el jugador eligió Salir (opción 4)
        if continuar_juego is False:
            break
    
    # Lógica de Fin de Juego
    print("\n--- ¡Fin de la Aventura! ---")
    if jugador.estaVivo():
        print(f"¡{jugador.nombre} ha salido de la aventura, vivo y sano!")
    else:
        print(f"La aventura de {jugador.nombre} ha terminado trágicamente. ¡Mejor suerte la próxima vez!")
    

def desarrolloJuego():
    jugador = comenzarAventura()
    
    while jugador.estaVivo():
        jugar(jugador)
    
    
comenzarAventura()





        



    
